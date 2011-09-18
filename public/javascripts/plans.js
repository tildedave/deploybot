var Plans = function (ele) {
  this.url = "/plans/";
  this.ele = ele;
};

Plans.prototype.load = function () {
  var parentObj = this;
  jQuery.get(this.url, function (data) {
    parentObj.populateOptions(data);
  });
};

Plans.prototype.bindEvents = function () {
  var ele = this.ele;

  ele.bind('change', function () {
    jQuery.publish("load-builds", jQuery(this).val());
  });

  jQuery.subscribe( 'select-plan', function (plan) {
    ele.val(plan);
  });
};

Plans.prototype.populateOptions = function (data) {
  var parentObj = this;
  var ele = this.ele;
  
  $.each(data.plans.plan, function (_, build) {
    ele.append($("<option></option>").
               attr("value", build.key).
               text(parentObj.getText(build)));
  });
  this.ele.trigger('change');
};

Plans.prototype.getText = function (build) {
  return build.key + " (" + build.name + ")";
};
