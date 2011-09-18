<head>
  <link rel="stylesheet" href="/public/styles.css" type="text/css" />
  <script type="text/javascript" src="/public/javascripts/jquery-1.6.4.min.js"></script>
  <script type="text/javascript" src="/public/javascripts/provider.js"></script>
  <script type="text/javascript" src="/public/javascripts/plans.js"></script>
  <script type="text/javascript" src="/public/javascripts/builds.js"></script>
  <script type="text/javascript" src="/public/javascripts/deployer.js"></script>
  <script type="text/javascript" src="/public/javascripts/deploybot.js"></script>
  <title>Deploybot</title>
</head>
<body>
  <a href="http://github.com/tildedave/deploybot"><img style="position: absolute; top: 0; right: 0; border: 0;" src="https://d3nwyuy0nl342s.cloudfront.net/img/7afbc8b248c68eb468279e8c17986ad46549fb71/687474703a2f2f73332e616d617a6f6e6177732e636f6d2f6769746875622f726962626f6e732f666f726b6d655f72696768745f6461726b626c75655f3132313632312e706e67" alt="Fork me on GitHub"></a>
  <div class="deploy">
    <h1>Deploybot</h1>

    <h2>Status</h2>
    <ul>
      <li><b>Version:</b> {{plan}}</li>
      <li><b>Build:</b> {{build}}</li>
    </ul>
    
    <h2>Deploy Build</h2>

    <div class="environments">
      <h3>Environment</h3>
      <select id="env-select">
        {% for environment in environments %}
        <option>{{ environment["name"] }}</option>
        {% end %}
      </select>
    </div>

    <div class="plans">
      <h3>Plan</h3>
      <select id="plan-select"></select>
    </div>

    <div class="builds">
      <h3>Build</h3>
      <select id="build-select"></select>
      <input id="build-deploy" type="button" value="Deploy!" />
      <span id="deploy-spinner"></span>
    </div>
  </div>

  <script type="text/javascript">
    jQuery(document).ready(function () {
        Deploybot.go("{{plan}}");
    });
  </script>
</body>
