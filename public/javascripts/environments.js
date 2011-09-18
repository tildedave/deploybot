(function (xhr) {
  "use strict";
  
  var EnvironmentsProvider = function () {
  };

  EnvironmentsProvider.prototype.get = function (callback) {
    jQuery.getJSON("/environments/", function (data) {
      callback(data);
    });
  };

  xhr.EnvironmentsProvider = EnvironmentsProvider;
  
}(xhr));

(function (exports, prov) {
  "use strict";

  var Environments = function (envSelector, plans) {
    this.envSelector = envSelector;
    this.plans = plans;
    this.provider = new prov.EnvironmentsProvider();
  };

  Environments.prototype.load = function (env) {
    this.provider.get(jQuery.proxy(this.renderEnvironments(env),
                                   this));
  };

  Environments.prototype.bindEvents = function () {
    var parentObj = this;
    this.envSelector.bind('change', function () {
      console.log("ZOMG CHANGE " + jQuery(this).val());
      parentObj.renderEnvironments(jQuery(this).val());
    });
  };
  
  Environments.prototype.renderEnvironments = function (env) {
    var plans = this.plans;
    
    return function (data) {
      var environments = jQuery(".status");
      var selectPlan = null;
      
      environments.empty();

      for(var i = 0, l = data.length; i < l; ++i) {
        var status = jQuery("#environment-status").tmpl(data[i]);
        status.appendTo(environments);

        if (env === data[i].plan) {
          selectPlan = data[i].plan;
        }
      }

      plans.load(selectPlan);
    };
  };

  exports.Environments = Environments;
  
}(window, provider));



