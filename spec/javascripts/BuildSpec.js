describe("Builds", function () {

  // stub
  var mockProvider = { get : function () { } };

  var build = function (build, time) {
    return {
      key : build,
      buildRelativeTime : time
    };
  };
  
  var mockHasBuilds = function (returnBuilds) {
    mockProvider.get = function (plan, obj) {
      obj.populateOptions({
        builds : {
          build : returnBuilds
        }
      });
    };
  };
  
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

  it("populates data from builds", function () {
    var builds = new Builds($(".builds"));
    builds.provider = mockProvider;

    mockHasBuilds([ build("EXAMPLE-TRUNK-1", "7 years ago"),
                    build("EXAMPLE-TRUNK-2", "Just now") ]);

    builds.load("EXAMPLE-TRUNK");

    var select = $("#build-select");
    expect(select.find("option").length).toBe(2);
  });

  it("has a value equal to the build key", function () {
    var builds = new Builds($(".builds"));
    builds.provider = mockProvider;

    mockHasBuilds([ build("EXAMPLE-TRUNK-15", "15 minutes ago") ]);

    builds.load("EXAMPLE-TRUNK");

    var select = $("#build-select");
    expect(select.find("option:first").val()).toEqual("EXAMPLE-TRUNK-15");
  });
  
  it("formats the builds", function () {
    var builds = new Builds($(".builds"));
    builds.provider = mockProvider;

    mockHasBuilds([ build("EXAMPLE-RELEASE-200", "3 hours ago")]);

    builds.load("EXAMPLE-RELEASE");

    var select = $("#build-select");
    expect(select.find("option:first").text())
      .toEqual("EXAMPLE-RELEASE-200 - 3 hours ago");
  });
});