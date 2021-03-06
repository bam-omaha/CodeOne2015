var app = angular.module('StarterApp', ['ngMaterial']).config(function($mdThemingProvider){
    $mdThemingProvider.theme('default')
        .primaryPalette('green');
        //.backgroundPalette('green');
});

app.controller('AppCtrl', ['$scope', '$mdSidenav', '$http', function($scope, $mdSidenav, $http){
    $scope.question = "";
    $scope.subject = "";
    $scope.hasInfo = false;
    $scope.isAnswer = true;
    $scope.isTabular = true;
    $scope.toggleSidenav = function(menuId) {
        $mdSidenav(menuId).toggle();
    };

    $scope.request = function(){
        console.log("SUBMIT TO TEAM BAM");
        console.log($scope.question);
        $http.post("/json/ask",{"question":$scope.question}).then(
                function(dat){
                    $scope.hasInfo=true;
                    console.log(dat);
                    if(dat.data.question_type=="What is"){
                        $scope.isTabular = false;
                        $scope.isAnswer = true;
                        $scope.answer = dat.data.answer;
                        $scope.subject = dat.data.table[0].topic_name;
                        console.log("WI");
                    }else {
                        $scope.isTabular = true;
                        $scope.isAnswer = true;
                        $scope.data = dat.data.table;
                        $scope.subject = "";
                    }
                      var audio = new Audio('static/holding.wav');
                      audio.play();
                    $scope.answer = dat.data.answer;
                },
                function(data, status){
                    $scope.hasInfo = false;
                    alert("malformed query");
                },angular.noop());


    }

}]);


app.directive('answerCard',function(){
    return {
        scope: {
            "answer" : "=answer",
            "subject" : "=subject"
        },
        templateUrl: '/html/answer.html'
    }
});
app.directive('splaininBox',function(){
    return {
        scope: {
            "data" : "=data"
        },
        templateUrl: '/html/splain.html'
    }
});
app.directive('awesomeGraph',function(){
    return {
        scope: {
            "data" : "=data"
        },
        templateUrl: '/html/graph.html',
        controller: 'GraphCtrl'
    }
});
app.controller('GraphCtrl', ['$scope', function($scope) {
    this._scope = $scope;
    $scope.points = [1,2,4];
    $scope.resolutions = {3600:[],604800:[]}

    $scope.mscale = .5;
    $scope.$watch('data', function(dat) {
        var points = [];
        $scope.minT=Infinity;
        $scope.maxT = 0;
        $scope.data.forEach(function(p){
            var t = Math.floor(new Date(p.time).getTime()/1000);
            $scope.minT = Math.min($scope.minT,t);
            $scope.maxT = Math.max($scope.maxT,t);
            points.push({t:t,amt:p.amount});
        });
        console.log($scope.minT);
        console.log($scope.maxT);
        $scope.minT = Math.floor($scope.minT/604800.0) * 604800;
        $scope.maxT = Math.ceil($scope.maxT/604800.0) * 604800;
        Object.keys($scope.resolutions).forEach(function(key){
            console.log(key);
            console.log($scope);
            var k=parseInt(key);
            console.log(parseInt($scope.maxT)/parseInt(key));
            var num = ($scope.maxT - $scope.minT )/parseInt(key);

            console.log(num);
            var arr = new Array(num);
            points.forEach(function(p){ 
                var i = Math.floor((p.t-$scope.minT)/key);
                if( arr[i] === undefined ){
                    arr[i] = 0;
                }
                arr[i] += parseFloat(p.amt);
            });
            $scope.resolutions[key] = arr;
        });
        console.log($scope.resolutions);


        console.log(points);
        $scope.points = points;
        console.log(dat);
        console.log($scope);
        console.log(this._scope);
        
    }, this);
    $scope.rescaleTime = function(time,width) {
        return width * (time-$scope.minT) / ($scope.maxT - $scope.minT);
    };
}]);
