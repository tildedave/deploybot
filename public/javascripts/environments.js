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

  var Environments = function (envSelector) {
    this.envSelector = envSelector;
    this.provider = new prov.EnvironmentsProvider();
  };

  Environments.prototype.load = function (env) {
    this.provider.get(jQuery.proxy(this.renderEnvironments(env),
                                   this));
  };
  
  Environments.prototype.bindEvents = function () {
    var envSelector = this.envSelector;
    var parentObj = this;
    
    this.envSelector.bind('change', function () {
      jQuery.publish( "new-environment", jQuery(this).val() );
    });

    jQuery.subscribe( "new-environment", function (env) {
      jQuery.proxy(parentObj.renderEnvironments(env), parentObj);
    });
  };
  
  Environments.prototype.renderEnvironments = function (env) {
    var envSelector = this.envSelector;
    return function (data) {
      var environments = jQuery(".status");
      environments.empty();

      for(var i = 0, l = data.length; i < l; ++i) {
        var status = jQuery("#environment-status").tmpl(data[i]);
        status.appendTo(environments);
      }

      envSelector.val(env);
    };
  };

  exports.Environments = Environments;
  
}(window, provider));