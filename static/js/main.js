var app = angular.module('StarterApp', ['ngMaterial']).config(function($mdThemingProvider){
    $mdThemingProvider.theme('default')
        .primaryPalette('green');
});

app.controller('AppCtrl', ['$scope', '$mdSidenav', function($scope, $mdSidenav){
    $scope.toggleSidenav = function(menuId) {
        $mdSidenav(menuId).toggle();
    };

}]);
