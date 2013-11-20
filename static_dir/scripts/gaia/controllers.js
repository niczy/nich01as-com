var phonecatControllers = angular.module('phonecatControllers', []);

phonecatControllers.controller('PhoneListCtrl', 
    ['$scope', '$http', function ($scope, $http) {
      $scope.phones = [
          {'name': 'Nexus S',
                 'snippet': 'Fast just got faster with Nexus S.'},
          {'name': 'Motorola XOOM™ with Wi-Fi',
                 'snippet': 'The Next, Next Generation tablet.'},
          {'name': 'MOTOROLA XOOM™',
                 'snippet': 'The Next, Next Generation tablet.'}];
    }]);
phonecatControllers.controller('PhoneDetailCtrl', 
    ['$scope', '$routeParams', function($scope, $routeParams) {
      $scope.phoneId = $routeParams.phoneId;
    }]);
phonecatControllers.controller('Signup1Ctrl', 
    ['$scope', '$routeParams', function($scope, $routeParams) {
      $scope.phoneId = $routeParams.phoneId;
    }]);
phonecatControllers.controller('Signup2Ctrl', 
    ['$scope', '$routeParams', function($scope, $routeParams) {
      $scope.phoneId = $routeParams.phoneId;
    }]);
phonecatControllers.controller('Signup3Ctrl', 
    ['$scope', '$routeParams', function($scope, $routeParams) {
      $scope.phoneId = $routeParams.phoneId;
    }]);
phonecatControllers.controller('Signup4Ctrl', 
    ['$scope', '$routeParams', function($scope, $routeParams) {
      $scope.phoneId = $routeParams.phoneId;
    }]);
phonecatControllers.controller('MainCtrl', function ($scope, $location) {
      $scope.go = function (path) {
                $location.path(path);
      }
});
