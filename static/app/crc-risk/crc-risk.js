'use strict';

angular.module('CRCRiskApp.risk', ['ngRoute','schemaForm', 'angular-loading-bar'])
	.config(['cfpLoadingBarProvider', function(cfpLoadingBarProvider) {
    	cfpLoadingBarProvider.latencyThreshold = 50;
    	cfpLoadingBarProvider.includeSpinner = false;
  		cfpLoadingBarProvider.includeBar = true;
  		cfpLoadingBarProvider.loadingBarTemplate = '<div id="loading-bar"><span class="fa">Working hard...</span><div class="bar"><div class="peg"></div></div></div>';

  	}])
	.controller('CRCRiskCtrl', ['$scope', '$rootScope', '$http', '$location','$timeout', 'cfpLoadingBar', function($scope, $rootScope, $http, $location, $timeout, cfpLoadingBar) {

		$scope.pretty = function(){
    		return typeof $scope.response === 'string' ? $scope.response : JSON.stringify($scope.response, undefined, 2);
    	};

    	var sections = ['demographics', 'diet', 'medical_history', 'medications', 'physical_activity', 'female_miscellaneous', 'family'];
    	//var sections = ['diet'];

	    var next_section = function (sectionId) {
	      $http.get('/static/app/asset/crc/' + sectionId + '.json').success(function(data) {
	        $scope.error = null;
	        $scope.loading = false;
	        $scope.schema = data.schema;
	        $scope.form = data.form;
	        $scope.response = {};
	        $scope.sectionId = sectionId;
	      }).error(function() {
	        $scope.error = 'Failed to load...';
	      });
	    };


	    $scope.submit = function(form) {
		    // First we broadcast an event so all fields validate themselves
		    $scope.$broadcast('schemaFormValidate');

		    // Then we check if the form is valid
		    if (form.$valid) {
		      // ... do whatever you need to do with your data.
		      if(responseForm.gender && responseForm.gender.value == "Male") {
		      	console.log(responseForm.gender.value);
		      	sections[4] = 'male_miscellaneous';
		      }
		      var next_sectionId = sections.shift();
		      if (next_sectionId) {
		      	next_section(next_sectionId);
		      }else{
              	cfpLoadingBar.start();

              	$timeout(function(){
              		cfpLoadingBar.complete();
              		$location.path('/risk-results');
              	},3000);
		      }
		    }
		}

		next_section(sections.shift());

		$rootScope.$on('cfpLoadingBar:completed', function(event){
          console.log(event);
      });

	}])
	.controller('CRCRiskResultsCtrl', ['$scope', '$http', '$location', function($scope,$http,$location) {

	}]);