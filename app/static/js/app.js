var kudisavers = angular.module('kudisavers', ['ui.bootstrap'])
	.config(function($interpolateProvider) {
        $interpolateProvider.startSymbol('{[{').endSymbol('}]}');
    });