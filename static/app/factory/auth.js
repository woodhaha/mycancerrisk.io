CRCRiskApp.factory('auth', [function() {
    var auth = {};

    auth.setAccessToken = function(accessToken) {
        auth.authToken = accessToken;
    }

    auth.getAccessToken = function() {
    	return auth.authToken;
    }
    
    return auth;
}])