describe("Deployer", function () {

  var envSelector;
  var planSelector;
  var buildSelector;
  var deployButton;
  var deploySpinner;

  var getMockEnvironments = function () {
    var environments = {
        load : function () {}
    };
    spyOn(environments, "load");
    
    return environments;
  };
  
  var getMockProvider = function () {
    var mockProvider = {
      deploy : function (data, callback) {
        callback.call();
      }
    };

    return mockProvider;
  };
  
  beforeEach(function () {
    envSelector = $("<select></select>");
    planSelector = $("<select></select>");
    buildSelector = $("<select></select>");
    deployButton = $('<input type="button" />');
    deploySpinner = $('<div id="deploy-spinner" />');
    
    var page = $('<div class="page" />');
    envSelector.appendTo(page);
    planSelector.appendTo(page);
    buildSelector.appendTo(page);
    deployButton.appendTo(page);
    deploySpinner.appendTo(page);    

    setFixtures(page);
  });
  
  it("sends a deploy instruction with the selected options", function () {
    var mockProvider = getMockProvider();
    spyOn(mockProvider, "deploy");

    jQuery("<option>vagrant</option>").appendTo(envSelector);
    jQuery("<option>PROJECT-PLAN</option>").appendTo(planSelector);
    jQuery("<option>PROJECT-PLAN-6</option>").appendTo(buildSelector);
    
    var deployer = new Deployer(deployButton, envSelector,
                                planSelector, buildSelector,
                                getMockEnvironments());
    deployer.provider = mockProvider;
    
    deployer.bindEvents();
    deployButton.click();

    expect(mockProvider.deploy).toHaveBeenCalled();
    var data = mockProvider.deploy.mostRecentCall.args[0];
    expect(data).toEqual({
      env : "vagrant", 
      plan : "PROJECT-PLAN",
      build : "PROJECT-PLAN-6"
    });
  });

  it("makes a spinner", function () {
    var mockProvider = getMockProvider();
    spyOn(mockProvider, "deploy");

    var deployer = new Deployer(deployButton, envSelector,
                                planSelector, buildSelector,
                                getMockEnvironments());
    deployer.provider = mockProvider;
    
    deployer.bindEvents();
    deployButton.click();

    var img = deploySpinner.children()[0];
    expect(img.src).toContain("spinner.gif");
  });

  it("makes a green checkbox", function () {
    var mockProvider = getMockProvider();

    var deployer = new Deployer(deployButton, envSelector,
                                planSelector, buildSelector,
                                getMockEnvironments());
    deployer.provider = mockProvider;
    
    deployer.bindEvents();
    deployButton.click();

    var img = deploySpinner.children()[0];
    expect(img.src).toContain("greenCheck.png");
  });

  it("loads environments after a deploy", function () {
    var environments = getMockEnvironments();
    var mockProvider = getMockProvider();

    var deployer = new Deployer(deployButton, envSelector,
                                planSelector, buildSelector,
                                environments);
    deployer.provider = mockProvider;

    deployer.bindEvents();
    deployButton.click();

    expect(environments.load).toHaveBeenCalled();
  });
});