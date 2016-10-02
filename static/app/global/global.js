'use strict';
// login page
angular.module('CRCRiskApp.global', ['ngRoute'])

/*.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/login', {
    templateUrl: '../static/app/login/login.html',
    controller: 'LoginCtrl'
  });
}])*/

.controller('GlobalCtrl', ['$scope','auth', '$location', '$http', function($scope, auth, $location, $http) {
    $scope.FBLogin = function() {
        FB.login(function(response) {
            if (response.authResponse) {
             console.log('Welcome!  Fetching your information.... ');
             FB.api('/me', function(response) {
               console.log('Good to see you, ' + response.name + '.');
               console.log(response);

               var accessToken =  FB.getAuthResponse().accessToken;
               console.log(accessToken);
               auth.setAccessToken(accessToken);

               $location.path('/about');
               $scope.$apply();
             });
            } else {
             console.log('User canceled login or did not fully authorize.');
            }
        });
    };

    $scope.FBlogout = function() {
        FB.logout(function(response) {
          console.log(response);
          auth.setAccessToken(null);
        // user is now logged out
            window.location.reload();
        });
    };

    $scope.isLoggedIn = function() {
      return auth.getAccessToken();
    };
    // $scope.showlist = function(){
    //              $http({
    //                  method: 'POST',
    //                  url: '/getTest',

    //              }).then(function(response) {
    //                  $scope.machines = response.data;
    //                  console.log('mm',$scope.machines);
    //              }, function(error) {
    //                  console.log(error);
    //              });
    //          }

}]);