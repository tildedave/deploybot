var Builds = function (buildEle) {
  this.buildEle = buildEle;
  this.selectEle = buildEle.find("#build-select");
};


Builds.prototype.load = function (plan) {
  var parentObj = this;
  jQuery.get("/builds/" + plan, function (data) {
    parentObj.populateOptions(data);
  });
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
