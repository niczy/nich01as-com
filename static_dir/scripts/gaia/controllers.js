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

phonecatControllers.controller('NavCtrl', function($scope, $rootScope, $location) {
    var styles = {
      left: ' \
        .page.ng-enter { \
          position:absolute; \
          -webkit-transition: 10.3s ease-out all; \
          -webkit-transform:translate3d(100%,0,0) ; \
        } \
        .page.ng-enter.ng-enter-active { \
          position:absolute; \
          -webkit-transform:translate3d(0,0,0) ; \
        } \
        .page.ng-leave { \
          position:absolute; \
          -webkit-transition: 10.3s ease-out all; \
          -webkit-transform:translate3d(0,0,0) ; \
        } \
        .page.ng-leave.ng-leave-active { \
          position:absolute; \
          -webkit-transform:translate3d(-100%,0,0) ; \
        }; \
      ',
     right: ' \
        .page.ng-enter { \
          position:absolute; \
          -webkit-transition: 10.3s ease-out all; \
          -webkit-transform:translate3d(-100%,0,0) ; \
        } \
        .page.ng-enter.ng-enter-active { \
          position:absolute; \
          -webkit-transform:translate3d(0,0,0) ; \
        } \
        .page.ng-leave { \
          position:absolute; \
          -webkit-transition: 10.3s ease-out all; \
          -webkit-transform:translate3d(0,0,0) ; \
        } \
        .page.ng-leave.ng-leave-active { \
          position:absolute; \
          -webkit-transform:translate3d(100%,0,0) ; \
        }; \
      ',
    };
    $scope.direction = function(dir) {
      $rootScope.style = styles[dir]
      console.log($rootScope.style);
    }
    $scope.goLast = function (path){
      $location.path(path);
    }

    $scope.goNext = function(path) {
      $location.path(path);
    }
});
