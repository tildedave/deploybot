describe("Builds", function () {

  // stub
  var mockProvider = { get : function () { } };
  
  beforeEach(function () {
    var html = '<div class="builds">' +
      '<h3>Builds</h3>' + 
      '<select id="build-select"></select>' + 
      '<input id="build-deploy" type="button" value="Deploy!" />' +
      '<span id="deploy-spinner"></span>' + 
      '</div>';

    setFixtures(html);
  });
  
  it("loads builds for a plan", function () {
    var builds = new Builds($(".builds"));
    builds.provider = mockProvider;
    spyOn(builds.provider, "get");

    builds.load("EXAMPLE-TRUNK");

    expect(builds.provider.get).toHaveBeenCalledWith("EXAMPLE-TRUNK", builds);
  });
});