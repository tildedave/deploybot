var Deploybot = {
  
  go : function (lastEnvironment) {
    
    // Build Selector
    var buildArea = jQuery(".builds");
    var buildSelector = buildArea.find("select");
    var builds = new Builds(buildArea);
    builds.bindEvents();

    // Plan Selector
    var planSelector = jQuery("#plan-select");
    var plans = new Plans(planSelector);
    plans.bindEvents();

    // Environments
    var envSelector = jQuery("#env-select");
    var environments = new Environments(envSelector);
    environments.bindEvents();
    envSelector.change();

    // Tail
    var tail = new Tail(jQuery("#deploy-tail"));
    tail.bindEvents();
    
    // Load data that won't change
    environments.load(lastEnvironment);
    plans.load();

    // Deploy button
    var deployButton = jQuery("#build-deploy");
    var deployer = new Deployer(deployButton, envSelector,
                                planSelector, buildSelector,
                                environments);
    deployer.bindEvents();
  }
};
