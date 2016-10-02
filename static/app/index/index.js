'use strict';
// login page
angular.module('CRCRiskApp.index', ['ngRoute'])

/*.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/login', {
    templateUrl: '../static/app/login/login.html',
    controller: 'LoginCtrl'
  });
}])*/

.controller('IndexCtrl', ['$scope','auth', '$location', '$http', function($scope, auth, $location, $http) {

	// $scope.showlist = function(){
	// 				$http({
	// 					method: 'POST',
	// 					url: '/getTest',

	// 				}).then(function(response) {
	// 					$scope.machines = response.data;
	// 					console.log('mm',$scope.machines);
	// 				}, function(error) {
	// 					console.log(error);
	// 				});
	// 			}

}]);