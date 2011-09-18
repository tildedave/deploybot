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

  var Environments = function () {
    this.provider = new prov.EnvironmentsProvider();
  };

  Environments.prototype.load = function () {
    console.log("ZOMG LOAD TIME");
    this.provider.get(jQuery.proxy(this.renderEnvironments, this));
  };

  Environments.prototype.renderEnvironments = function (data) {
    var environments = jQuery(".status");
    environments.empty();

    for(var i = 0, l = data.length; i < l; ++i) {
      var status = jQuery("#environment-status").tmpl(data[i]);
      status.appendTo(environments);
    }
  };

  exports.Environments = Environments;
  
}(window, provider));