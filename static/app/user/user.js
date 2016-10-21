'use strict';

angular.module('CRCRiskApp.user', ['ngRoute','schemaForm'])

	.controller('UserCtrl', ['$scope','$rootScope', '$http',function($scope, $rootScope, $http) {
		$scope.form_user = [
		    "fname",
		    "lname",
		    "age",
		    "email",
		    "Phone",
		    {
		      "type": "submit",
		      "style": "btn-info",
		      "title": "Submit"
		    }
		];

		$scope.schema_user = {
		    "type": "object",
		    "properties": {
		    	"fname": {
		      		"type": "string",
		        	"minLength": 2,
		        	"title": "First Name"
		      	},
		      	"lname": {
		      		"type": "string",
		        	"minLength": 2,
		        	"title": "Last Name"
		      	},
		       	"age": {
			    	"title": "Age",
				    "type": "number"
			    },
			    "email": {
			    	"title": "Email",
				    "type": "string",
				    "pattern": "^\\S+@\\S+$"
			    },
			    "Phone": {
			    	"title": "Phone Number",
			    	"type": "string",
			    	"pattern": "^[0-9]*$"
			    }
		    },
		     "required": [
			    "fname",
			    "lname",
			    "age",
			    "email",
			    "Phone"
			  ]
		};
		$scope.response_user = {};
		$scope.submit = function(form) {
		    // First we broadcast an event so all fields validate themselves
            $scope.$broadcast('schemaFormValidate');
            // Then we check if the form is valid
            if (form.$valid) {
            	$http({
                  method: 'POST',
                  url: '/update',
                  data: {
                      info: $scope.response_user
                  }
                  }).then(function(response) {
                      console.log(response.data.message);
                  }, function(error) {
                      console.log(error);
                  });
            }
		}
}]);