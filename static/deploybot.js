var Deploybot = {
  
  go : function (lastPlan) {
    var planSelector = jQuery("#plan-select");
    var buildArea = jQuery(".builds");
    var buildSelector = buildArea.find("select");

    var builds = new Builds(buildArea);
    var plans = new Plans(planSelector, builds, lastPlan);

    plans.bindEvents();
    plans.load(lastPlan);
    
    this.bindDeployButton("build-deploy", planSelector, buildSelector);
  },

  bindDeployButton: function (buttonId, planSelector, buildSelector) {  
    jQuery("#" + buttonId).bind('click', function () {
      var plan = planSelector.val();
      var build = buildSelector.val();
      
      var data = {
        "plan": plan,
        "build": build
      };

      var spinner = jQuery("#deploy-spinner");
      spinner.html('<img src="static/spinner.gif">');
      jQuery.post("/deploy/", data, function () {
        spinner.html('<img src="static/greenCheck.png"> Deployed');
      });
    });
  }
};