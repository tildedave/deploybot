describe("Deployer", function () {

  var envSelector;
  var planSelector;
  var buildSelector;
  var deployButton;

  var getMockProvider = function () {
    var mockProvider = {
      deploy : function (data, callback) {
        callback.call();
      }
    };
    spyOn(mockProvider, "deploy");

    return mockProvider;
  };
  
  beforeEach(function () {
    envSelector = $("<select></select>");
    planSelector = $("<select></select>");
    buildSelector = $("<select></select>");
    deployButton = $('<input type="button" />');
    
    var page = $('<div class="page" />');
    envSelector.appendTo(page);
    planSelector.appendTo(page);
    buildSelector.appendTo(page);
    deployButton.appendTo(page);

    setFixtures(page);
  });
  
  it("sends a deploy instruction with the selected options", function () {
    var mockProvider = getMockProvider();

    jQuery("<option>vagrant</option>").appendTo(envSelector);
    jQuery("<option>PROJECT-PLAN</option>").appendTo(planSelector);
    jQuery("<option>PROJECT-PLAN-6</option>").appendTo(buildSelector);
    
    var deployer = new Deployer(deployButton, envSelector,
                                planSelector, buildSelector);
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
  
});