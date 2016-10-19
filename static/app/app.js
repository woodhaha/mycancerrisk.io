'use strict';
var _env = {};

// Declare app level module which depends on views, and components
var CRCRiskApp = angular.module('CRCRiskApp', [
  'ngRoute',
  'CRCRiskApp.risk',
  'CRCRiskApp.about',
  'CRCRiskApp.user',
  'CRCRiskApp.version',
  'CRCRiskApp.global'
]);
CRCRiskApp.config(['$routeProvider', function($routeProvider) {
  $routeProvider
    .when('/', {
    // templateUrl: '../static/app/index/index.html',
    // controller: 'IndexCtrl'
    redirectTo: '/about'
  })
    .when('/about', {
    templateUrl: '../static/app/about/about.html',
    controller: 'AboutCtrl'
  })
    .when('/risk', {
    templateUrl: '../static/app/crc-risk/crc-risk.html',
    controller: 'CRCRiskCtrl'
  })
    .when('/risk-results', {
    templateUrl: '../static/app/crc-risk/crc-risk-results.html',
    controller: 'CRCRiskResultsCtrl'
  })
    .when('/user', {
    templateUrl: '../static/app/user/user.html',
    controller: 'UserCtrl'
  })
  .otherwise({redirectTo: '/about'});
}])

CRCRiskApp.run(['$rootScope', '$location', '$window', '$routeParams',
  function($rootScope,$location,$window,$routeParams) {

    $rootScope.$on('$routeChangeSuccess', function(e, current, pre) {
      var route = $location.path().substring(1);
      console.log('Current route name: ' + route);
      // Get all URL parameter
      //console.log($routeParams);
      angular.element(document.querySelector('.nav.navbar-nav > li.active')).removeClass('active');
      if (route != '') {
        angular.element(document.querySelector('.nav.navbar-nav > li#' + route)).addClass('active');
      }
    });

}]);

// Import variables if present(from env.js)
if(window){
  Object.assign(__env, window.__env);
}




