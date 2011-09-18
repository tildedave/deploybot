var Deploybot = {
  
  go : function (lastPlan) {
    var envSelector = jQuery("#env-select");

    // Environments
    var environments = new Environments();
    environments.load();
    
    // Build Selector
    var buildArea = jQuery(".builds");
    var buildSelector = buildArea.find("select");
    var builds = new Builds(buildArea);

    // Plan Selector
    var planSelector = jQuery("#plan-select");
    var plans = new Plans(planSelector, builds, lastPlan);
    plans.bindEvents();
    plans.load(lastPlan);

    // Deploy button
    var deployButton = jQuery("#build-deploy");
    var deployer = new Deployer(deployButton, envSelector,
                                planSelector, buildSelector,
                                environments);
    deployer.bindEvents();
  }
};
