%%javascript
"use strict";

require.undef('cyjs');

define('cyjs', ["jupyter-js-widgets", "cytoscape"], function(widgets, cytoscape) {
    
    var CyjsView = widgets.DOMWidgetView.extend({

        initialize: function() {
           this.circles = [];
           this.circleCount = 0;
           this.options = {}; 
           this.msg = "empty in javascript";
           this.msgToKernel = "";
           this.msgFromKernel = "";
           this.defaultHeight = "800px";
           this.defaultWidth = "1000px";
           },

        createDiv: function(){
            var outerDiv = $("<div id='cyOuterDiv' style='border:1px solid gray; height: 800px; width: 1000px'></div>");
            var toolbarDiv = $("<div id='cyToolbarDiv' style='height: 30px; width: 1000px'></div>");
            var cyDiv = $("<div id='cyDiv' style='height: 870px; width: 1000px'></div>");
            outerDiv.append(toolbarDiv);
            outerDiv.append(cyDiv);
            var cyWidget = this;
            var fitButton = $("<button>Fit</button>").click(function(){
                console.log("Fit!");
                console.log("fitButton's notion of this:")
                console.log(cyWidget.cy);
                cyWidget.cy.fit(50);
               });
            toolbarDiv.append(fitButton);
            var fitSelectedButton = $("<button>Fit Selected</button>").click(function(){
                var selectedNodes = cyWidget.cy.filter('node:selected');
                if(selectedNodes.length > 0){
                   cyWidget.cy.fit(selectedNodes, 50);
                   }
               });
            toolbarDiv.append(fitSelectedButton);
            var sfnButton = $("<button>SFN</button>").click(function(){
               cyWidget.cy.nodes(':selected').neighborhood().nodes().select()
               });
            toolbarDiv.append(sfnButton);
            var clearButton = $("<button>Clear</button>").click(function(){
               cyWidget.cy.nodes().unselect();
               cyWidget.cy.edges().unselect();
               });
            toolbarDiv.append(clearButton);
            return(outerDiv);
           },
 
        
        createCanvas: function(){
            var cyjsWidget = this;
            console.log("createCanvas notion of this:")
            console.log(cyjsWidget);
            this.cy = cytoscape({
               container: document.getElementById('cyDiv'),
               //elements: {
               //nodes: [
               //  {data: {id: 'a', name: 'Node A', type: 'big' }},
               //  {data: {id: 'b', name: 'Node B', type: 'little'}},
               //  ],
              //edges: [
              //  {data: {source: 'a', target: 'b'}},
              //         {data: {source: 'b', target: 'a'}}
              // ]},
          ready: function(){
            console.log("small cyjs network ready");
            console.log("ready's notion of this:")
            console.log(this);
            cyjsWidget.cy = this;
            window.cy = this;  // for easy debugging
            console.log("ready's notion of cyjsWidget:")
            console.log(cyjsWidget);
            console.log("calling this.fit")
            //cyWidget.cy.fit(100);
            console.log("--- about to call loadGraph")
            cyjsWidget.loadGraph("network.json");
            cyjsWidget.loadStyle("style.js");
            console.log("    back from loadGraph")
            cyjsWidget.cy.on("select", function(x){
                var selectedNodeCount = cyjsWidget.cy.nodes(":selected").length;
                var selectedEdgeCount = cyjsWidget.cy.edges(":selected").length;
                console.log("selected nodes: " + selectedNodeCount);
                console.log("selected edges:" + selectedEdgeCount);
                });
            cyjsWidget.cy.on("unselect", function(x){
                var selectedNodeCount = cyjsWidget.cy.nodes(":selected").length;
                var selectedEdgeCount = cyjsWidget.cy.edges(":selected").length;
                console.log("selected nodes: " + selectedNodeCount);
                console.log("selected edges:" + selectedEdgeCount);
                });
            } // ready
           })},

        loadStyle: function(filename){
           var cyObj = this.cy;
           console.log("cyjsWidget.loadStyle: " + filename)
           console.log("loadStyle's notion of this:");
           console.log(this);
           console.log("loadStyle's notion of cy:");
           console.log(cyObj);
           var str = window.location.href;
           var url = str.substr(0, str.lastIndexOf("/")) + "/" + filename;
           url = url.replace("/notebooks/", "/files/");
           console.log("about to getScript: " + url);
           $.getScript(url)
              .done(function(script, textStatus){
                 console.log("loadStyle: " + textStatus);
                 cyObj.style(vizmap);
                 })
             .fail(function(jqxhr, settings, exception){
                console.log("loadStyle error trying to read " + filename);
                console.log("exception: ");
                console.log(exception);
                });
          },
        
        loadGraph: function(filename){
           console.log("entering loadGraph");
           var cyObj = this.cy;
              // the robust url of a file in the same directory as the notebook is
              // str.substring(0, str.lastIndexOf("/"));
           var str = window.location.href;
           var url = str.substr(0, str.lastIndexOf("/")) + "/" + filename;
           url = url.replace("/notebooks/", "/files/");
           console.log("=== about to getScript on " + url);
           $.getScript(url)
              .done(function(script, textStatus) {
                 console.log("getScript: " + textStatus);
                 console.log("nodes: " + network.elements.nodes.length);
                 if(typeof(network.elements.edges) != "undefined")
                    console.log("edges: " + network.elements.edges.length);
                cyObj.add(network.elements);  // no positions yet
                cyObj.nodes().map(function(node){node.data({degree: node.degree()})});
                cyObj.fit(150);
                }) // .done
            .fail(function(jqxhr, settings, exception) {
               console.log("addNetwork getscript error trying to read " + filename);
               });
           },
        
        render: function() { 
            console.log("entering render")
            this.$el.append(this.createDiv());
            this.listenTo(this.model, 'change:frameWidth', this.frameDimensionsChanged, this);
            this.listenTo(this.model, 'change:frameHeight', this.frameDimensionsChanged, this);
            this.listenTo(this.model, 'change:msgFromKernel', this.dispatchRequest, this);
            var cyjsWidget = this;
            function myFunc(){
               cyjsWidget.createCanvas()
               }
            setTimeout(myFunc, 500);
            },

        dispatchRequest: function(){
           console.log("dispatchRequest");
           var msgRaw = this.model.get("msgFromKernel");
           var msg = JSON.parse(msgRaw);
           console.log(msg);
           console.log("========================");
           console.log(this);
           switch(msg.cmd) {
              case 'cleanSlate':
                 console.log("got request to cleanSlate");
                 break;
              case 'fit':
                 var margin = msg.payload;
                 console.log("fit with margin: " + margin)
                 this.cy.fit(margin);
                 break;
              case 'getSelectedNodes':
                 var selectedNodes = this.cy.filter("node:selected").map(function(node){ 
                     return node.data().id});
                  console.log("-- found these selected nodes: ");
                  console.log(selectedNodes);
                  var jsonString = JSON.stringify({cmd: "storeSelectedNodes",
                                                   status: "reply",
                                                   callback: "",
                                                   payload: selectedNodes})
                  console.log(" *** jsonString: ")
                  console.log(jsonString);
                  this.model.set("msgToKernel", jsonString);
                  console.log("    after setting 'msgToKernel");
                  this.touch();
                  break;
               case 'selectNodes':
                  var nodeIDs = msg.payload;
                  console.log("--- selecting these nodes: " + nodeIDs);
                  if(typeof(nodeIDs) == "string")
                     nodeIDs = [nodeIDs];
                 var filterStrings = [];
                 for(var i=0; i < nodeIDs.length; i++){
                   var s = '[id="' + nodeIDs[i] + '"]';
                   filterStrings.push(s);
                   } // for i
                var nodesToSelect = this.cy.nodes(filterStrings.join());
                nodesToSelect.select()
                break;
              case 'clearSelection':
                 this.cy.nodes().unselect();
                 break;
            default:
               console.log("unrecognized msg.cmd: " + msg.cmd);
             } // switch
           console.log("CONCLUDING dispatchRequest")
           }, 
        
        frameDimensionsChanged: function(){
           console.log("frameDimensionsChanged")
           var newWidth  = this.model.get("frameWidth");
           var newHeight = this.model.get("frameHeight");
           console.log("frame: " + newWidth + " x " + newHeight);
           $("#cyOuterDiv").width(newWidth);
           $("#cyOuterDiv").height(newHeight);
           $("#cyToolbarDiv").width(newWidth);
           $("#cyDiv").width(newWidth);
           $("#cyDiv").height(newHeight - $("#cyToolbarDiv").height());
           }, 
        
        events: {
           //"click #svg": "changeHandler"
           }

    });
    return {
        CyjsView: CyjsView
    };
});