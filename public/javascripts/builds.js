(function (xhr) {
  "use strict";

  var BuildsProvider = function () {
  };

  BuildsProvider.prototype.get = function (plan, builds) {
    jQuery.get("/builds/" + plan, function (data) {
      builds.populateOptions(data);
    });
  };

  xhr.BuildsProvider = BuildsProvider;
}(xhr));

(function (exports, prov) {
  "use strict";
  
  var Builds = function (buildEle) {
    this.buildEle = buildEle;
    this.selectEle = buildEle.find("#build-select");
    this.provider = new prov.BuildsProvider();
  };

  Builds.prototype.bindEvents = function () {
    var parentObj = this;
    var provider = this.provider;
    
    jQuery.subscribe( "load-builds", function (plan) {
      provider.get(plan, parentObj);
    });
  };

  Builds.prototype.load = function (plan) {
    this.provider.get(plan, this);
  };

  Builds.prototype.populateOptions = function (data) {
    var parentObj = this;
    var selectEle = this.selectEle;

    selectEle.empty();
    $.each(data.builds.build, function (_, build) {
      selectEle.append(
        $("<option></option>").
          attr("value", build.key).
          text(parentObj.getText(build)));
    });    

    selectEle.trigger('change');
  };

  Builds.prototype.getText = function (build) {
    return build.key + " - " + build.buildRelativeTime;
  };

  exports.Builds = Builds;
}(window, provider));