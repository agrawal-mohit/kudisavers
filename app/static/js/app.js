var kudisavers = angular.module('kudisavers', [])
	.config(function($interpolateProvider) {
        $interpolateProvider.startSymbol('{[{').endSymbol('}]}');
    });