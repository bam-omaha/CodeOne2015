var app = angular.module('StarterApp', ['ngMaterial']).config(function($mdThemingProvider){
    $mdThemingProvider.theme('default')
        .primaryPalette('green');
        //.backgroundPalette('green');
});

app.controller('AppCtrl', ['$scope', '$mdSidenav', '$http', function($scope, $mdSidenav, $http){
    $scope.data = [1,2,3,4];
    $scope.toggleSidenav = function(menuId) {
        $mdSidenav(menuId).toggle();
    };

    $scope.request = function(){
        console.log("SUBMIT TO TEAM BAM");
        console.log($scope.question);
        $http.post("/json/ask",{"question":$scope.question}).then(
                function(dat){
                    console.log(dat);
                    $scope.data = dat.data.table;
                },
                function(data, status){
                    alert("malformed query")
                },angular.noop());

    }

}]);


app.directive('splaininBox',function(){
    return {
        scope: {
            "data" : "=data"
        },
        templateUrl: '/html/splain.html'
    }
});
