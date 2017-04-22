'use strict';

angular.module('CRCRiskApp.risk-results', ['ngRoute','schemaForm'])
    .controller('CRCRiskResultsCtrl', ['$scope', '$http', '$location', function($scope,$http,$location) {
        $scope.pretty = function(){
            return typeof $scope.response === 'string' ? $scope.response : JSON.stringify($scope.response, undefined, 2);
        };
        $http.get("/getResult")
             .success(function (response) {
              // console.log('absRsk: ' + response['absRsk']);
              // console.log('CI: ' + response['CI']);
              $scope.risk = response['absRsk'];
              $scope.CI = response['CI'];
              $scope.average_risk = response['avgrisk'];
             }).error(function(error) {
                console.log(error);
             });
    }]);