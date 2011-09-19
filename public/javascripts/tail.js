(function (exports, prov) {
  "use strict";

  var Tail = function (ele) {
    this.ele = ele;
  };

  Tail.prototype.bindEvents = function () {
    var ele = this.ele;
    
    jQuery.subscribe( "deploy", function () {
      jQuery.get( "/tail/", function (data) {
        ele.html("<pre>" + data + "</pre>");
      });
    });
  };

  exports.Tail = Tail;
}(window, provider));
