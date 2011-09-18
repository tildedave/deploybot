var Deploybot = {
  
  go : function (lastEnvironment) {
    
    // Build Selector
    var buildArea = jQuery(".builds");
    var buildSelector = buildArea.find("select");
    var builds = new Builds(buildArea);

    // Plan Selector
    var planSelector = jQuery("#plan-select");
    var plans = new Plans(planSelector, builds);
    plans.bindEvents();

    // Environments
    var envSelector = jQuery("#env-select");
    var environments = new Environments(envSelector, plans);
    environments.bindEvents();
    environments.load(lastEnvironment);
    envSelector.change();

    // Deploy button
    var deployButton = jQuery("#build-deploy");
    var deployer = new Deployer(deployButton, envSelector,
                                planSelector, buildSelector,
                                environments);
    deployer.bindEvents();
  }
};
