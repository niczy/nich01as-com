var phonecatApp = angular.module('phonecatApp', [
      'ngRoute',
        'phonecatControllers',
        'ngAnimate'
]);

phonecatApp.config(['$routeProvider',
    function($routeProvider) {
        $routeProvider.
        when('/signup/1', {
          templateUrl: '/s/htmls/partials/signup-1.html',
          controller: "Signup1Ctrl"
        }).
        when('/signup/2', {
          templateUrl: '/s/htmls/partials/signup-2.html',
          controller: "Signup2Ctrl"
        }).
        when('/signup/3', {
          templateUrl: '/s/htmls/partials/signup-3.html',
          controller: "Signup3Ctrl"
        }).
        when('/signup/4', {
          templateUrl: '/s/htmls/partials/signup-4.html',
          controller: "Signup4Ctrl"
        }).
        when('/phones', {
            templateUrl: '/s/htmls/partials/phone-list.html',
            controller: 'PhoneListCtrl'
        }).
        when('/phones/:phoneId', {
            templateUrl: 'partials/phone-detail.html',
            controller: 'PhoneDetailCtrl'
        }).
        when('/one', {
            templateUrl: 'page1.html',
            controller: 'MainCtrl'
        }).
        when('/two', {
            templateUrl: 'page2.html',
            controller: 'MainCtrl'
        }).
        otherwise({
            redirectTo: '/phones'
            });
    }]);


