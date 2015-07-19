'use strict';

var routines = angular.module('routinesApp', [
    'ngRoute',
    'ui.bootstrap',
    'angular-loading-bar',
]);

routines.config(['$routeProvider', function($routeProvider){
    $routeProvider
    .when('/', {
        templateUrl: 'views/routines.html',
        controller: 'routinesController'
    })
    .otherwise({
        redirectTo: '/'
    });
}]);
