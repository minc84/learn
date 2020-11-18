(function(g){var window=this;var N5=function(a,b){var c="ytp-miniplayer-button-bottom-right",d={I:"svg",U:{height:"18px",version:"1.1",viewBox:"0 0 22 18",width:"22px"},S:[{I:"g",U:{fill:"none","fill-rule":"evenodd",stroke:"none","stroke-width":"1"},S:[{I:"g",U:{transform:"translate(-1.000000, -3.000000)"},S:[{I:"polygon",U:{points:"0 0 24 0 24 24 0 24"}},{I:"path",U:{d:"M19,7 L5,7 L5,17 L19,17 L19,7 Z M23,19 L23,4.98 C23,3.88 22.1,3 21,3 L3,3 C1.9,3 1,3.88 1,4.98 L1,19 C1,20.1 1.9,21 3,21 L21,21 C22.1,21 23,20.1 23,19 Z M21,19.02 L3,19.02 L3,4.97 L21,4.97 L21,19.02 Z",
fill:"#fff","fill-rule":"nonzero"}}]}]}]},e="\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0443 \u043f\u0440\u043e\u0441\u043c\u043e\u0442\u0440\u0430";a.T().ca("kevlar_miniplayer_expand_top")&&(c="ytp-miniplayer-button-top-left",d={I:"svg",U:{height:"24px",version:"1.1",viewBox:"0 0 24 24",width:"24px"},S:[{I:"g",U:{fill:"none","fill-rule":"evenodd",stroke:"none","stroke-width":"1"},S:[{I:"g",U:{transform:"translate(12.000000, 12.000000) scale(-1, 1) translate(-12.000000, -12.000000) "},
S:[{I:"path",U:{d:"M19,19 L5,19 L5,5 L12,5 L12,3 L5,3 C3.89,3 3,3.9 3,5 L3,19 C3,20.1 3.89,21 5,21 L19,21 C20.1,21 21,20.1 21,19 L21,12 L19,12 L19,19 Z M14,3 L14,5 L17.59,5 L7.76,14.83 L9.17,16.24 L19,6.41 L19,10 L21,10 L21,3 L14,3 Z",fill:"#fff","fill-rule":"nonzero"}}]}]}]},e="\u0420\u0430\u0437\u0432\u0435\u0440\u043d\u0443\u0442\u044c");g.V.call(this,{I:"button",ia:["ytp-miniplayer-expand-watch-page-button","ytp-button",c],U:{title:"{{title}}","data-tooltip-target-id":"ytp-miniplayer-expand-watch-page-button"},
S:[d]});this.J=a;this.va("click",this.onClick,this);this.xa("title",g.XX(a,e,"i"));g.dg(this,g.vY(b.Ib(),this.element))},O5=function(a){g.V.call(this,{I:"div",
L:"ytp-miniplayer-ui"});this.eh=!1;this.player=a;this.R(a,"minimized",this.yi);this.R(a,"onStateChange",this.SQ)},P5=function(a){g.HS.call(this,a);
this.u=new O5(this.player);this.u.hide();g.EP(this.player,this.u.element,4);a.app.visibility.u&&(this.load(),g.K(a.getRootNode(),"ytp-player-minimized",!0))};
g.u(N5,g.V);N5.prototype.onClick=function(){this.J.ua("onExpandMiniplayer")};g.u(O5,g.V);g.k=O5.prototype;
g.k.show=function(){this.Gd=new g.qn(this.Lp,null,this);this.Gd.start();if(!this.eh){this.tooltip=new g.K_(this.player,this);g.C(this,this.tooltip);g.EP(this.player,this.tooltip.element,4);this.tooltip.scale=.6;this.Lb=new g.pY(this.player);g.C(this,this.Lb);this.Ik=new g.V({I:"div",L:"ytp-miniplayer-scrim"});g.C(this,this.Ik);this.Ik.fa(this.element);this.R(this.Ik.element,"click",this.wE);var a=new g.V({I:"button",ia:["ytp-miniplayer-close-button","ytp-button"],U:{"aria-label":"\u0417\u0430\u043a\u0440\u044b\u0442\u044c"},S:[g.IN()]});
g.C(this,a);a.fa(this.Ik.element);this.R(a.element,"click",this.vn);a=new N5(this.player,this);g.C(this,a);a.fa(this.Ik.element);this.jl=new g.V({I:"div",L:"ytp-miniplayer-controls"});g.C(this,this.jl);this.jl.fa(this.Ik.element);this.R(this.jl.element,"click",this.wE);var b=new g.V({I:"div",L:"ytp-miniplayer-button-container"});g.C(this,b);b.fa(this.jl.element);a=new g.V({I:"div",L:"ytp-miniplayer-play-button-container"});g.C(this,a);a.fa(this.jl.element);var c=new g.V({I:"div",L:"ytp-miniplayer-button-container"});
g.C(this,c);c.fa(this.jl.element);this.UE=new g.LZ(this.player,this,!1);g.C(this,this.UE);this.UE.fa(b.element);b=new g.IZ(this.player,this);g.C(this,b);b.fa(a.element);this.nextButton=new g.LZ(this.player,this,!0);g.C(this,this.nextButton);this.nextButton.fa(c.element);this.Gh=new g.z_(this.player,this);g.C(this,this.Gh);this.Gh.fa(this.Ik.element);this.Pc=new g.PZ(this.player,this);g.C(this,this.Pc);g.EP(this.player,this.Pc.element,4);this.Ws=new g.V({I:"div",L:"ytp-miniplayer-buttons"});g.C(this,
this.Ws);g.EP(this.player,this.Ws.element,4);a=new g.V({I:"button",ia:["ytp-miniplayer-close-button","ytp-button"],U:{"aria-label":"\u0417\u0430\u043a\u0440\u044b\u0442\u044c"},S:[g.IN()]});g.C(this,a);a.fa(this.Ws.element);this.R(a.element,"click",this.vn);a=new g.V({I:"button",ia:["ytp-miniplayer-replay-button","ytp-button"],U:{"aria-label":"\u0417\u0430\u043a\u0440\u044b\u0442\u044c"},S:[g.VN()]});g.C(this,a);a.fa(this.Ws.element);this.R(a.element,"click",this.WO);this.R(this.player,"presentingplayerstatechange",
this.Wb);this.R(this.player,"appresize",this.Ra);this.R(this.player,"fullscreentoggled",this.Ra);this.Ra();this.eh=!0}0!==this.player.getPlayerState()&&g.V.prototype.show.call(this);this.Pc.show();this.player.unloadModule("annotations_module")};
g.k.hide=function(){this.Gd&&(this.Gd.dispose(),this.Gd=void 0);g.V.prototype.hide.call(this);this.player.app.visibility.u||(this.eh&&this.Pc.hide(),this.player.loadModule("annotations_module"))};
g.k.aa=function(){this.Gd&&(this.Gd.dispose(),this.Gd=void 0);g.V.prototype.aa.call(this)};
g.k.vn=function(){this.player.stopVideo();this.player.ua("onCloseMiniplayer")};
g.k.WO=function(){this.player.playVideo()};
g.k.wE=function(a){if(a.target===this.Ik.element||a.target===this.jl.element)g.R(this.player.T().experiments,"kevlar_miniplayer_play_pause_on_scrim")?g.zL(g.DI(this.player))?this.player.pauseVideo():this.player.playVideo():this.player.ua("onExpandMiniplayer")};
g.k.yi=function(){g.K(this.player.getRootNode(),"ytp-player-minimized",this.player.app.visibility.u)};
g.k.Zd=function(){this.Pc.Gc();this.Gh.Gc()};
g.k.Lp=function(){this.Zd();this.Gd&&this.Gd.start()};
g.k.Wb=function(a){g.U(a.state,32)&&this.tooltip.hide()};
g.k.Ra=function(){this.Pc.setPosition(0,g.WG(this.player).getPlayerSize().width,!1);g.RZ(this.Pc)};
g.k.SQ=function(a){this.player.app.visibility.u&&(0===a?this.hide():this.show())};
g.k.Ib=function(){return this.tooltip};
g.k.Jd=function(){return!1};
g.k.If=function(){return!1};
g.k.hh=function(){return!1};
g.k.vy=function(){};
g.k.ll=function(){};
g.k.Go=function(){};
g.k.wl=function(){return null};
g.k.ci=function(){return new g.ig(0,0,0,0)};
g.k.handleGlobalKeyDown=function(){return!1};
g.k.handleGlobalKeyUp=function(){return!1};
g.k.Dn=function(a,b,c,d,e){var f=0,h=d=0,l=g.Eg(a);if(b){c=g.zn(b,"ytp-prev-button")||g.zn(b,"ytp-next-button");var m=g.zn(b,"ytp-play-button"),n=g.zn(b,"ytp-miniplayer-expand-watch-page-button");c?f=h=12:m?(b=g.Cg(b,this.element),h=b.x,f=b.y-12):n&&(h=g.zn(b,"ytp-miniplayer-button-top-left"),f=g.Cg(b,this.element),b=g.Eg(b),h?(h=8,f=f.y+40):(h=f.x-l.width+b.width,f=f.y-20))}else h=c-l.width/2,d=25+(e||0);b=g.WG(this.player).getPlayerSize().width;e=f+(e||0);l=g.be(h,0,b-l.width);e?(a.style.top=e+
"px",a.style.bottom=""):(a.style.top="",a.style.bottom=d+"px");a.style.left=l+"px"};
g.k.showControls=function(){};
g.k.Ej=function(){};
g.k.bj=function(){return!1};g.u(P5,g.HS);P5.prototype.create=function(){};
P5.prototype.Ch=function(){return!1};
P5.prototype.load=function(){this.player.hideControls();this.u.show()};
P5.prototype.unload=function(){this.player.showControls();this.u.hide()};g.JX.miniplayer=P5;})(_yt_player);
