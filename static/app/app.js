'use strict';
var _env = {};

// Declare app level module which depends on views, and components
var CRCRiskApp = angular.module('CRCRiskApp', [
  'ngRoute',
  'CRCRiskApp.index',
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

CRCRiskApp.run(['$rootScope', '$location', '$window', '$routeParams', 'auth',
  function($rootScope,$location,$window,$routeParams,auth) {
    $window.fbAsyncInit = function(_env) {
        FB.init({
          appId      : __env.facebook.appId,
          cookie     : __env.facebook.cookie,
          status     : __env.facebook.status,
          xfbml      : __env.facebook.xfbml,
          version    : __env.facebook.version
        });
    };

    (function(d, s, id){
       var js, fjs = d.getElementsByTagName(s)[0];
       if (d.getElementById(id)) {return;}
       js = d.createElement(s); js.id = id;
       js.src = "//connect.facebook.net/en_US/sdk.js";
       fjs.parentNode.insertBefore(js, fjs);
     }(document, 'script', 'facebook-jssdk'));

    $rootScope.$on('$routeChangeStart', function(event, next, current) {
        /*If route is authenticated, then the user should have access token*/
        //console.log(event);
        //console.log(current);
        //console.log(next);
        // if (next.$$route.authenticated) {
        //     if (!auth.getAccessToken()) {
        //       $location.path('/about');
        //     }
        // }
    });

    $rootScope.$on('$routeChangeSuccess', function(e, current, pre) {
      var route = $location.path().substring(1);
      console.log('Current route name: ' + route);
      // Get all URL parameter
      //console.log($routeParams);
      angular.element(document.querySelector('.nav.navbar-nav > li.active')).removeClass('active');
      angular.element(document.querySelector('.nav.navbar-nav > li#' + route)).addClass('active');

    });

}]);

// Import variables if present(from env.js)
if(window){
  Object.assign(__env, window.__env);
}




