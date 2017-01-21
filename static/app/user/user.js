'use strict';

angular.module('CRCRiskApp.user', ['ngRoute','schemaForm'])

	.controller('UserCtrl', ['$scope','$rootScope', '$http', '$window',function($scope, $rootScope, $http) {

		$scope.form_user = [
		    {
		    	"key": "fname",
		    	"placeholder": ""
		    },
		    {
		    	"key": "lname",
		    	"placeholder": ""
		    },
		    {
		    	"key": "age",
		    	"placeholder": ""
		    },
		    {
		    	"key": "email",
		    	"placeholder": "test@gmail.com"
		    },
		    {
		    	"key": "phone",
		    	"placeholder": ""
		    },
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
			    "phone": {
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
		$scope.response_user={};
		$http.get("/getUserInfo")
			.success(function (response) {
				$scope.response_user = response;
			}).error(function(error) {
				console.log(error);
			});
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
	 //    console.log(UserData);
}]);