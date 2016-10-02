'use strict';

angular.module('CRCRiskApp.user', ['ngRoute','schemaForm'])

	.controller('UserCtrl', ['$scope',function($scope) {
		$scope.schema1 = {
		    type: "object",
		    properties: {
		    	fname: {
		      		type: "string",
		        	minLength: 2,
		        	title: "First Name"
		      	},
		      	lname: {
		      		type: "string",
		        	minLength: 2,
		        	title: "Last Name"
		      	},
		       	age: {
			    	title: "Age",
				    type: "number"
			    },
			    email: {
			    	title: "Email",
				    type: "string",
				    pattern: "^\\S+@\\S+$"
			    },
			    Phone: {
			    	title: "Phone Number",
			    	type: "string",
			    	pattern: "^[0-9]*$"
			    }
		    }
		};

		$scope.form1 = [
		    {
		    	key: "fname"
		    },
		    {
		    	key: "lname"
		    },
		    {
		    	key: "age"
		    },
		    {
		    	key: "email"
		    },
		    {
		    	key: "Phone"
		    },
		    {
		        type: "submit",
		        title: "Save",
		        htmlClass: "save_bt"
		    }
		];
		$scope.model1 = {};
}]);