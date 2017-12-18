const Alexa = require('alexa-sdk');
const http = require("http");

exports.handler = (event, context, callback) => {
    var alexa = Alexa.handler(event, context);
    alexa.appId = undefined;
    alexa.registerHandlers(handlers);
    alexa.execute();
}

const handlers = {
    'PhaticIntent': function () {
        this.emit(':responseReady');
    },    
    'ControlLights': function() {
        var team = this.event.request.intent.slots.Team.value;
        var self = this;
        changeLights(team, function() {
            self.response.speak("OK! Let's go " + team);
            self.emit(':responseReady');
        });
    },
    'AMAZON.StopIntent': function () {
        var self = this;
        changeLights("off", function() {
            self.response.speak("OK! Lights off.");
            self.emit(':responseReady');
        });
    }
};

// Do the HTTP post in a separate function with callback. See https://stackoverflow.com/a/42444397
function changeLights(team, callback) {
    var postData = 'team=' + team;
    var options = {
        hostname: 'www.johnriendeau.com',
        port: 80,
        path: '/lights/index.php',
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Content-Length': postData.length
        }
    };
    
    var req = http.request(options, function(res) {
      return callback();
    });
    req.write(postData);
    req.end();
}
