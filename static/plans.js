var Plans = function (ele, builds) {
  this.url = "/plans/";
  this.ele = ele;
  this.builds = builds;
}

Plans.prototype.load = function (lastPlan) {
  var parentObj = this;
  jQuery.get(this.url, function (data) {
    parentObj.populateOptions(data, lastPlan);
  });
};

Plans.prototype.bindEvents = function () {
  var builds = this.builds;
  this.ele.bind('change', function () {
    builds.load(jQuery(this).val());
  });
};

Plans.prototype.populateOptions = function (data, lastPlan) {
  var parentObj = this;
  var ele = this.ele;
  
  $.each(data.plans.plan, function (_, build) {
    ele.append($("<option></option>").
               attr("value", build.key).
               text(parentObj.getText(build)));
  });
  this.ele.val(lastPlan);
  this.ele.trigger('change');
};

Plans.prototype.getText = function (build) {
  return build.key + " (" + build.name + ")";
};
