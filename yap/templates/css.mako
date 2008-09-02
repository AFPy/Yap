# -*- coding: utf-8 -*-
/* ${'='*(len(c.theme)+14)} */
/* CSS for ${c.theme} theme */
/* ${'='*(len(c.theme)+14)} */
%for k,v in c.values.items():
/*    ${k}: ${v} */
%endfor

body{
 background:${c.bg_color2} url(${c.base_url}/bg_body.gif) repeat-x;
}

.item{
	margin: 0px 10px 20px 10px;
	background-color: ${c.bg_color2};
	border: solid ${c.color1} 1px;
}

.itemBody{
	width: 100%;
	height: 50px;
}

.itemTitle {
	width: 100%;
	height: 25px;
	background-color: ${c.bg_color1};
	cursor: move;
}

div.cmDiv {
    background-color: ${c.bg_color1};
	border: solid ${c.color1} 1px;
}

.clickMenu li.main,
.clickMenu ul {
    color:${c.color2};
    background-color: ${c.bg_color1};
}

.clickMenu a {
    color:${c.color2};
    text-decoration:none;
    padding: 0em 1em;
    display:block;
}

.clickMenu li.main li {
    padding: 0;
}

.clickMenu li.main li a {
    width:100px;
    padding: 0.2em 1em;
}

.clickMenu li:hover,
.clickMenu a:hover {
    color: ${c.bg_color2};
    background: ${c.color2};
}

div.login {
    float:right;
    color: ${c.color2};
    padding-right:2em;
    padding-top:2px;
}
div.search_form {
    float:right;
    color: ${c.color2};
    padding-right:1em;
}

/* boxes options */

.boxMenuHeader {
    color:${c.color2};
    background-color: ${c.bg_color1};
    border-bottom: thin solid ${c.color1};
}

.boxMenuBody {
    border-bottom: thin solid ${c.color1};
}

/* boxes overides */


.boxGhost{
	border: dashed ${c.color1} 1px;
}

.message{
	border: solid black 1px;
	background-color: ${c.bg_color1};
}

.uiNoteTextArea{
	background-color: ${c.color2};
}

.uiBox{
	border: solid ${c.color1} 1px;
	overflow: hidden;
}

.uiBoxHeader{
  color:${c.color2};
	background-color: ${c.bg_color1};
}

.uiBoxBody{
	background-color: ${c.color2};
}

/* feed item */

.feedItem {
    margin-bottom:0.2em;
}

.feedTitle {
    color: ${c.bg_color1};
}

.feedDescription {
    font-size:90%;
}

/* album */

.uiAlbumPrev,
.uiAlbumNext {
    color: ${c.bg_color1};
}

/* popup */

#list_boxes {
    width:100%;
    height:375px;
    overflow:auto;
}

#list_boxes a {
    display:block;
    color: ${c.color1};
	background-color: ${c.bg_color1};
	border: solid ${c.color1} 1px;
    text-decoration:none;
    text-align: center;
    margin-bottom:3px;
}

/* Link Box */

.linkItem a {
    color: ${c.bg_color1};
}

