(function (xhr) {
  "use strict";

  var DeployProvider = function () {
  };

  DeployProvider.prototype.deploy = function (data, callback) { 
    jQuery.post("/deploy/", data, function (response) {
      callback(response);
    });
  };

  xhr.DeployProvider = DeployProvider;
  
}(xhr));


(function (exports, prov) {
  "use strict";
  
  var Deployer = function (ele, envSelector, planSelector, buildSelector) {
    this.ele = ele;
    this.envSelector = envSelector;
    this.planSelector = planSelector;
    this.buildSelector = buildSelector;
    this.provider = new prov.DeployProvider();
  };

  Deployer.prototype.bindEvents = function () {
    jQuery(this.ele).bind('click', jQuery.proxy(this.deploy, this));
  };

  Deployer.prototype.deploy = function () {
    var env = this.envSelector.val();
    var plan = this.planSelector.val();
    var build = this.buildSelector.val();

    var data = {
      "env" : env,
      "plan": plan,
      "build": build
    };

    var spinner = jQuery("#deploy-spinner");
    spinner.html('<img src="public/spinner.gif">');
    this.provider.deploy(data, function (response) {
      if (response.success) {
        spinner.html('<span class="success"><img src="public/greenCheck.png">Deployed</span>');
      }
      else {
        spinner.html('<span class="failure"><img src="public/failure.png"> Failed to Deploy :(</span>');          
      }
      jQuery.publish( "deploy" );
    });
  };

  exports.Deployer = Deployer;
}(window, provider));
