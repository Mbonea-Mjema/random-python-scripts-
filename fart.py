Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from requests import Session as s
>>> tab=s()
>>> response=tab.get('https://www.premierleague.com/tables')
>>> from bs4 import BeautifulSoup as bs
>>> soup =bs(response.text,'html.parser')
>>> table=soup.findAll('div' ,'class':"table wrapper col-12")
SyntaxError: invalid syntax
>>> table=soup.findAll('div' ,{'class':"table wrapper col-12"})
>>> table
[<div class="table wrapper col-12">
<table>
<summary class="visuallyHidden">This table charts the Premier League teams</summary>
<thead>
<tr>
<th class="revealMoreHeader text-centre" scope="col" style="display:none;">More</th>
<th class="text-centre" scope="col">
<div class="thFull">Position</div>
<div class="thShort">Pos</div>
</th>
<th class="team" scope="col">Club</th>
<th scope="col">
<div class="thFull">Played</div>
<div class="thShort">Pl</div>
</th>
<th scope="col">
<div class="thFull">Won</div>
<div class="thShort">W</div>
</th>
<th scope="col">
<div class="thFull">Drawn</div>
<div class="thShort">D</div>
</th>
<th scope="col">
<div class="thFull">Lost</div>
<div class="thShort">L</div>
</th>
<th class="hideSmall" scope="col"><abbr title="Goals For">GF</abbr></th>
<th class="hideSmall" scope="col"><abbr title="Goals Against">GA</abbr></th>
<th scope="col"><abbr title="Goal Difference">GD</abbr></th>
<th class="points" scope="col">
<div class="thFull">Points</div>
<div class="thShort">Pts</div>
</th>
<th class="teamForm hideMed" scope="col">Form</th>
<th class="hideMed text-centre" scope="col">Next</th>
</tr>
</thead>
<tbody class="tableBodyContainer">
<tr class="tableDark" data-compseason="79" data-filtered-entry-size="20" data-filtered-table-row="11" data-filtered-table-row-abbr="11" data-filtered-table-row-name="Manchester City" data-filtered-table-row-opta="t43">
<td class="revealMore" role="button" style="display:none;" tabindex="0">
<div class="icn chevron-down-g"></div>
</td>
<td class="pos button-tooltip" id="Tooltip" role="tooltip" tabindex="0">
<span class="value">1</span>
<span class="movement none">
<span class="tooltipContainer tooltip-left" role="tooltip">
<span class="tooltip-content">Previous Position
                            <span class="resultHighlight">
                                1
                            </span>
</span>
</span>
</span>
</td>
<td class="team" scope="row">
<a href="/clubs/11/Manchester-City/overview"><span alt="" class="badge-25 t43"></span><span class="long">Manchester City</span><span class="short">MCI</span></a>
</td>
<td>7</td>
<td>6</td>
<td>1</td>
<td>0</td>
<td class="hideSmall">22</td>
<td class="hideSmall">2</td>
<td> 
        +20

 </td>
<td class="points">19</td>
<td class="form hideMed">
<ul>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/22362" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 26 August 2017</span>
<span class="teamName">BOU</span>
<span class="badge-20 t91"></span>
<span class="score">1 <span>-</span>2</span>
<span class="badge-20 t43"></span>
<span class="teamName">MCI</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/22377" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 9 September 2017</span>
<span class="teamName">MCI</span>
<span class="badge-20 t43"></span>
<span class="score">5 <span>-</span>0</span>
<span class="badge-20 t14"></span>
<span class="teamName">LIV</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/22390" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 16 September 2017</span>
<span class="teamName">WAT</span>
<span class="badge-20 t57"></span>
<span class="score">0 <span>-</span>6</span>
<span class="badge-20 t43"></span>
<span class="teamName">MCI</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/22397" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 23 September 2017</span>
<span class="teamName">MCI</span>
<span class="badge-20 t43"></span>
<span class="score">5 <span>-</span>0</span>
<span class="badge-20 t31"></span>
<span class="teamName">CRY</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/22404" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 30 September 2017</span>
<span class="teamName">CHE</span>
<span class="badge-20 t8"></span>
<span class="score">0 <span>-</span>1</span>
<span class="badge-20 t43"></span>
<span class="teamName">MCI</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
</ul>
<td class="nextMatchCol hideMed">
<span class="button-tooltip" id="Tooltip" role="tooltip" tabindex="0">
<span class="nextMatch"><span class="badge-20 t110"><span class="visuallyHidden">Stoke City</span></span></span>
<a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/22417" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 14 October 2017</span>
<span class="teamName">MCI</span>
<span class="badge-20 t43"></span>
<time>15:00</time>
<span class="badge-20 t110"></span>
<span class="teamName">STK</span>
<span class="icn arrow-right"></span>
</div></span>
</a></span></td></td></tr></tbody></table></div>, <div class="table wrapper col-12">
<table>
<summary class="visuallyHidden">This table charts the Premier League teams</summary>
<thead>
<tr>
<th class="text-centre" scope="col">
<div class="thFull">Position</div>
<div class="thShort">Pos</div>
</th>
<th class="team" scope="col">Club</th>
<th scope="col">
<div class="thFull">Played</div>
<div class="thShort">Pl</div>
</th>
<th scope="col">
<div class="thFull">Won</div>
<div class="thShort">W</div>
</th>
<th scope="col">
<div class="thFull">Drawn</div>
<div class="thShort">D</div>
</th>
<th scope="col">
<div class="thFull">Lost</div>
<div class="thShort">L</div>
</th>
<th class="hideSmall" scope="col"><abbr title="Goals For">GF</abbr></th>
<th class="hideSmall" scope="col"><abbr title="Goals Against">GA</abbr></th>
<th scope="col"><abbr title="Goal Difference">GD</abbr></th>
<th class="points" scope="col">
<div class="thFull">Points</div>
<div class="thShort">Pts</div>
</th>
<th class="teamForm hideMed" scope="col">Form</th>
<th class="hideMed text-centre" scope="col">Next</th>
</tr>
</thead>
<tbody class="tableBodyContainer">
<tr class="tableDark" data-compseason="39" data-filtered-entry-size="12" data-filtered-table-row="387" data-filtered-table-row-abbr="387" data-filtered-table-row-name="Man Utd" data-filtered-table-row-opta="t6826">
<td class="pos" tabindex="0">
<span class="value">1</span>
</td>
<td class="team" scope="row">
<a href="/clubs/12/Manchester-United/overview"><span alt="" class="badge-25 t6826"></span><span class="long">Manchester United</span><span class="short">MUN</span></a>
</td>
<td>22</td>
<td>15</td>
<td>3</td>
<td>4</td>
<td class="hideSmall">44</td>
<td class="hideSmall">19</td>
<td> 
        +25

 </td>
<td class="points">48</td>
<td class="form hideMed">
<ul>
<li class="draw button-tooltip" id="Tooltip" role="tooltip" tabindex="0">D
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13736" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 4 April 2016</span>
<span class="teamName">MUN</span>
<span class="badge-20 t6826"></span>
<span class="score">1 <span>-</span>1</span>
<span class="badge-20 t7140"></span>
<span class="teamName">CHE</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13749" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 11 April 2016</span>
<span class="teamName">MUN</span>
<span class="badge-20 t6826"></span>
<span class="score">1 <span>-</span>0</span>
<span class="badge-20 t7138"></span>
<span class="teamName">MID</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13760" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Tuesday 19 April 2016</span>
<span class="teamName">TOT</span>
<span class="badge-20 t1175"></span>
<span class="score">2 <span>-</span>3</span>
<span class="badge-20 t6826"></span>
<span class="teamName">MUN</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13764" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 25 April 2016</span>
<span class="teamName">SOU</span>
<span class="badge-20 t1189"></span>
<span class="score">2 <span>-</span>1</span>
<span class="badge-20 t6826"></span>
<span class="teamName">MUN</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13768" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Friday 6 May 2016</span>
<span class="teamName">CHE</span>
<span class="badge-20 t7140"></span>
<span class="score">0 <span>-</span>1</span>
<span class="badge-20 t6826"></span>
<span class="teamName">MUN</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
</ul>
<td class="nextMatchCol hideMed">
</td>
</td>
</tr>
<tr class="expandable" data-filtered-table-row-expander="387">
<td colspan="13">
<a class="expandableTeam" href="/clubs/12/Manchester-United/overview">
<span class="badge-50 t6826"></span>
<span class="teamName">Manchester United</span>
</a>
<div class="expandableFixtures">
<div class="resultWidget">
<div class="label"><strong>Recent Result</strong> - Monday 4 April 2016</div>
<a class="matchAbridged pre" href="/match/13768">
<span class="teamName">CHE</span>
<span class="badge-20 t7140"></span>
<span class="score">0 <span>-</span>1</span>
<span class="badge-20 t6826"></span>
<span class="teamName">MUN</span>
<span class="icn arrow-right"></span>
</a>
</div>
<div class="btnContainer">
<a class="btn-highlight" href="/clubs/12/Manchester-United/overview" role="btn">Visit <span class="visuallyHidden">Manchester United </span>Club Page<span class="icn arrow-right-w"></span></a>
</div>
</div>
<div class="teamPerformanceStandingsArea" style="display:none;">
<header>
<h3 class="subHeader left">Performance Chart</h3>
<a class="btn right" href="/stats/comparison">Compare against another team<span class="icn arrow-right"></span></a>
</header>
<div class="teamPerformanceStandingsContainer"></div>
</div>
</td>
</tr>
<tr class="" data-compseason="39" data-filtered-entry-size="12" data-filtered-table-row="355" data-filtered-table-row-abbr="355" data-filtered-table-row-name="Sunderland" data-filtered-table-row-opta="t819">
<td class="pos" tabindex="0">
<span class="value">2</span>
</td>
<td class="team" scope="row">
<a href="/clubs/29/Sunderland/overview"><span alt="" class="badge-25 t819"></span><span class="long">Sunderland</span><span class="short">SUN</span></a>
</td>
<td>22</td>
<td>13</td>
<td>4</td>
<td>5</td>
<td class="hideSmall">38</td>
<td class="hideSmall">20</td>
<td> 
        +18

 </td>
<td class="points">43</td>
<td class="form hideMed">
<ul>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13705" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 7 March 2016</span>
<span class="teamName">SUN</span>
<span class="badge-20 t819"></span>
<span class="score">3 <span>-</span>2</span>
<span class="badge-20 t7592"></span>
<span class="teamName">EVE</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="draw button-tooltip" id="Tooltip" role="tooltip" tabindex="0">D
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13715" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 12 March 2016</span>
<span class="teamName">MCI</span>
<span class="badge-20 t1050"></span>
<span class="score">1 <span>-</span>1</span>
<span class="badge-20 t819"></span>
<span class="teamName">SUN</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13727" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 21 March 2016</span>
<span class="teamName">MID</span>
<span class="badge-20 t7138"></span>
<span class="score">0 <span>-</span>1</span>
<span class="badge-20 t819"></span>
<span class="teamName">SUN</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="draw button-tooltip" id="Tooltip" role="tooltip" tabindex="0">D
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13732" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Sunday 3 April 2016</span>
<span class="teamName">SUN</span>
<span class="badge-20 t819"></span>
<span class="score">2 <span>-</span>2</span>
<span class="badge-20 t1189"></span>
<span class="teamName">SOU</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13752" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 11 April 2016</span>
<span class="teamName">TOT</span>
<span class="badge-20 t1175"></span>
<span class="score">3 <span>-</span>1</span>
<span class="badge-20 t819"></span>
<span class="teamName">SUN</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
</ul>
<td class="nextMatchCol hideMed">
</td>
</td>
</tr>
<tr class="expandable" data-filtered-table-row-expander="355">
<td colspan="13">
<a class="expandableTeam" href="/clubs/29/Sunderland/overview">
<span class="badge-50 t819"></span>
<span class="teamName">Sunderland</span>
</a>
<div class="expandableFixtures">
<div class="resultWidget">
<div class="label"><strong>Recent Result</strong> - Monday 7 March 2016</div>
<a class="matchAbridged pre" href="/match/13752">
<span class="teamName">TOT</span>
<span class="badge-20 t1175"></span>
<span class="score">3 <span>-</span>1</span>
<span class="badge-20 t819"></span>
<span class="teamName">SUN</span>
<span class="icn arrow-right"></span>
</a>
</div>
<div class="btnContainer">
<a class="btn-highlight" href="/clubs/29/Sunderland/overview" role="btn">Visit <span class="visuallyHidden">Sunderland </span>Club Page<span class="icn arrow-right-w"></span></a>
</div>
</div>
<div class="teamPerformanceStandingsArea" style="display:none;">
<header>
<h3 class="subHeader left">Performance Chart</h3>
<a class="btn right" href="/stats/comparison">Compare against another team<span class="icn arrow-right"></span></a>
</header>
<div class="teamPerformanceStandingsContainer"></div>
</div>
</td>
</tr>
<tr class="" data-compseason="39" data-filtered-entry-size="12" data-filtered-table-row="339" data-filtered-table-row-abbr="339" data-filtered-table-row-name="Everton" data-filtered-table-row-opta="t7592">
<td class="pos" tabindex="0">
<span class="value">3</span>
</td>
<td class="team" scope="row">
<a href="/clubs/7/Everton/overview"><span alt="" class="badge-25 t7592"></span><span class="long">Everton</span><span class="short">EVE</span></a>
</td>
<td>22</td>
<td>10</td>
<td>7</td>
<td>5</td>
<td class="hideSmall">35</td>
<td class="hideSmall">27</td>
<td> 
        +8

 </td>
<td class="points">37</td>
<td class="form hideMed">
<ul>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13737" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 4 April 2016</span>
<span class="teamName">NOR</span>
<span class="badge-20 t6920"></span>
<span class="score">1 <span>-</span>2</span>
<span class="badge-20 t7592"></span>
<span class="teamName">EVE</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13747" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 11 April 2016</span>
<span class="teamName">EVE</span>
<span class="badge-20 t7592"></span>
<span class="score">2 <span>-</span>0</span>
<span class="badge-20 t7140"></span>
<span class="teamName">CHE</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13757" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 18 April 2016</span>
<span class="teamName">EVE</span>
<span class="badge-20 t7592"></span>
<span class="score">1 <span>-</span>0</span>
<span class="badge-20 t1050"></span>
<span class="teamName">MCI</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13761" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 25 April 2016</span>
<span class="teamName">EVE</span>
<span class="badge-20 t7592"></span>
<span class="score">3 <span>-</span>1</span>
<span class="badge-20 t8755"></span>
<span class="teamName">LEI</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="draw button-tooltip" id="Tooltip" role="tooltip" tabindex="0">D
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13766" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 2 May 2016</span>
<span class="teamName">CHE</span>
<span class="badge-20 t7140"></span>
<span class="score">0 <span>-</span>0</span>
<span class="badge-20 t7592"></span>
<span class="teamName">EVE</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
</ul>
<td class="nextMatchCol hideMed">
</td>
</td>
</tr>
<tr class="expandable" data-filtered-table-row-expander="339">
<td colspan="13">
<a class="expandableTeam" href="/clubs/7/Everton/overview">
<span class="badge-50 t7592"></span>
<span class="teamName">Everton</span>
</a>
<div class="expandableFixtures">
<div class="resultWidget">
<div class="label"><strong>Recent Result</strong> - Monday 4 April 2016</div>
<a class="matchAbridged pre" href="/match/13766">
<span class="teamName">CHE</span>
<span class="badge-20 t7140"></span>
<span class="score">0 <span>-</span>0</span>
<span class="badge-20 t7592"></span>
<span class="teamName">EVE</span>
<span class="icn arrow-right"></span>
</a>
</div>
<div class="btnContainer">
<a class="btn-highlight" href="/clubs/7/Everton/overview" role="btn">Visit <span class="visuallyHidden">Everton </span>Club Page<span class="icn arrow-right-w"></span></a>
</div>
</div>
<div class="teamPerformanceStandingsArea" style="display:none;">
<header>
<h3 class="subHeader left">Performance Chart</h3>
<a class="btn right" href="/stats/comparison">Compare against another team<span class="icn arrow-right"></span></a>
</header>
<div class="teamPerformanceStandingsContainer"></div>
</div>
</td>
</tr>
<tr class="" data-compseason="39" data-filtered-entry-size="12" data-filtered-table-row="381" data-filtered-table-row-abbr="381" data-filtered-table-row-name="Man City" data-filtered-table-row-opta="t1050">
<td class="pos" tabindex="0">
<span class="value">4</span>
</td>
<td class="team" scope="row">
<a href="/clubs/11/Manchester-City/overview"><span alt="" class="badge-25 t1050"></span><span class="long">Manchester City</span><span class="short">MCI</span></a>
</td>
<td>22</td>
<td>10</td>
<td>4</td>
<td>8</td>
<td class="hideSmall">35</td>
<td class="hideSmall">26</td>
<td> 
        +9

 </td>
<td class="points">34</td>
<td class="form hideMed">
<ul>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13731" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Friday 1 April 2016</span>
<span class="teamName">MID</span>
<span class="badge-20 t7138"></span>
<span class="score">3 <span>-</span>1</span>
<span class="badge-20 t1050"></span>
<span class="teamName">MCI</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13751" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 11 April 2016</span>
<span class="teamName">RDG</span>
<span class="badge-20 t7608"></span>
<span class="score">0 <span>-</span>3</span>
<span class="badge-20 t1050"></span>
<span class="teamName">MCI</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13757" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 18 April 2016</span>
<span class="teamName">EVE</span>
<span class="badge-20 t7592"></span>
<span class="score">1 <span>-</span>0</span>
<span class="badge-20 t1050"></span>
<span class="teamName">MCI</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13769" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Friday 6 May 2016</span>
<span class="teamName">MCI</span>
<span class="badge-20 t1050"></span>
<span class="score">2 <span>-</span>0</span>
<span class="badge-20 t7139"></span>
<span class="teamName">LIV</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13770" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 9 May 2016</span>
<span class="teamName">MCI</span>
<span class="badge-20 t1050"></span>
<span class="score">0 <span>-</span>1</span>
<span class="badge-20 t7140"></span>
<span class="teamName">CHE</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
</ul>
<td class="nextMatchCol hideMed">
</td>
</td>
</tr>
<tr class="expandable" data-filtered-table-row-expander="381">
<td colspan="13">
<a class="expandableTeam" href="/clubs/11/Manchester-City/overview">
<span class="badge-50 t1050"></span>
<span class="teamName">Manchester City</span>
</a>
<div class="expandableFixtures">
<div class="resultWidget">
<div class="label"><strong>Recent Result</strong> - Friday 1 April 2016</div>
<a class="matchAbridged pre" href="/match/13770">
<span class="teamName">MCI</span>
<span class="badge-20 t1050"></span>
<span class="score">0 <span>-</span>1</span>
<span class="badge-20 t7140"></span>
<span class="teamName">CHE</span>
<span class="icn arrow-right"></span>
</a>
</div>
<div class="btnContainer">
<a class="btn-highlight" href="/clubs/11/Manchester-City/overview" role="btn">Visit <span class="visuallyHidden">Manchester City </span>Club Page<span class="icn arrow-right-w"></span></a>
</div>
</div>
<div class="teamPerformanceStandingsArea" style="display:none;">
<header>
<h3 class="subHeader left">Performance Chart</h3>
<a class="btn right" href="/stats/comparison">Compare against another team<span class="icn arrow-right"></span></a>
</header>
<div class="teamPerformanceStandingsContainer"></div>
</div>
</td>
</tr>
<tr class="" data-compseason="39" data-filtered-entry-size="12" data-filtered-table-row="336" data-filtered-table-row-abbr="336" data-filtered-table-row-name="Chelsea" data-filtered-table-row-opta="t7140">
<td class="pos" tabindex="0">
<span class="value">5</span>
</td>
<td class="team" scope="row">
<a href="/clubs/4/Chelsea/overview"><span alt="" class="badge-25 t7140"></span><span class="long">Chelsea</span><span class="short">CHE</span></a>
</td>
<td>22</td>
<td>9</td>
<td>6</td>
<td>7</td>
<td class="hideSmall">34</td>
<td class="hideSmall">30</td>
<td> 
        +4

 </td>
<td class="points">33</td>
<td class="form hideMed">
<ul>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13763" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 25 April 2016</span>
<span class="teamName">MID</span>
<span class="badge-20 t7138"></span>
<span class="score">1 <span>-</span>3</span>
<span class="badge-20 t7140"></span>
<span class="teamName">CHE</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="draw button-tooltip" id="Tooltip" role="tooltip" tabindex="0">D
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13766" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 2 May 2016</span>
<span class="teamName">CHE</span>
<span class="badge-20 t7140"></span>
<span class="score">0 <span>-</span>0</span>
<span class="badge-20 t7592"></span>
<span class="teamName">EVE</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13768" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Friday 6 May 2016</span>
<span class="teamName">CHE</span>
<span class="badge-20 t7140"></span>
<span class="score">0 <span>-</span>1</span>
<span class="badge-20 t6826"></span>
<span class="teamName">MUN</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13770" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 9 May 2016</span>
<span class="teamName">MCI</span>
<span class="badge-20 t1050"></span>
<span class="score">0 <span>-</span>1</span>
<span class="badge-20 t7140"></span>
<span class="teamName">CHE</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13772" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Thursday 12 May 2016</span>
<span class="teamName">LEI</span>
<span class="badge-20 t8755"></span>
<span class="score">3 <span>-</span>0</span>
<span class="badge-20 t7140"></span>
<span class="teamName">CHE</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
</ul>
<td class="nextMatchCol hideMed">
</td>
</td>
</tr>
<tr class="expandable" data-filtered-table-row-expander="336">
<td colspan="13">
<a class="expandableTeam" href="/clubs/4/Chelsea/overview">
<span class="badge-50 t7140"></span>
<span class="teamName">Chelsea</span>
</a>
<div class="expandableFixtures">
<div class="resultWidget">
<div class="label"><strong>Recent Result</strong> - Monday 25 April 2016</div>
<a class="matchAbridged pre" href="/match/13772">
<span class="teamName">LEI</span>
<span class="badge-20 t8755"></span>
<span class="score">3 <span>-</span>0</span>
<span class="badge-20 t7140"></span>
<span class="teamName">CHE</span>
<span class="icn arrow-right"></span>
</a>
</div>
<div class="btnContainer">
<a class="btn-highlight" href="/clubs/4/Chelsea/overview" role="btn">Visit <span class="visuallyHidden">Chelsea </span>Club Page<span class="icn arrow-right-w"></span></a>
</div>
</div>
<div class="teamPerformanceStandingsArea" style="display:none;">
<header>
<h3 class="subHeader left">Performance Chart</h3>
<a class="btn right" href="/stats/comparison">Compare against another team<span class="icn arrow-right"></span></a>
</header>
<div class="teamPerformanceStandingsContainer"></div>
</div>
</td>
</tr>
<tr class="" data-compseason="39" data-filtered-entry-size="12" data-filtered-table-row="352" data-filtered-table-row-abbr="352" data-filtered-table-row-name="Southampton" data-filtered-table-row-opta="t1189">
<td class="pos" tabindex="0">
<span class="value">6</span>
</td>
<td class="team" scope="row">
<a href="/clubs/20/Southampton/overview"><span alt="" class="badge-25 t1189"></span><span class="long">Southampton</span><span class="short">SOU</span></a>
</td>
<td>22</td>
<td>8</td>
<td>6</td>
<td>8</td>
<td class="hideSmall">39</td>
<td class="hideSmall">40</td>
<td> 
        -1

 </td>
<td class="points">30</td>
<td class="form hideMed">
<ul>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13719" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 14 March 2016</span>
<span class="teamName">MID</span>
<span class="badge-20 t7138"></span>
<span class="score">1 <span>-</span>3</span>
<span class="badge-20 t1189"></span>
<span class="teamName">SOU</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13725" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Sunday 20 March 2016</span>
<span class="teamName">LIV</span>
<span class="badge-20 t7139"></span>
<span class="score">0 <span>-</span>5</span>
<span class="badge-20 t1189"></span>
<span class="teamName">SOU</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="draw button-tooltip" id="Tooltip" role="tooltip" tabindex="0">D
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13732" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Sunday 3 April 2016</span>
<span class="teamName">SUN</span>
<span class="badge-20 t819"></span>
<span class="score">2 <span>-</span>2</span>
<span class="badge-20 t1189"></span>
<span class="teamName">SOU</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13758" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 18 April 2016</span>
<span class="teamName">SOU</span>
<span class="badge-20 t1189"></span>
<span class="score">3 <span>-</span>2</span>
<span class="badge-20 t6920"></span>
<span class="teamName">NOR</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13764" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 25 April 2016</span>
<span class="teamName">SOU</span>
<span class="badge-20 t1189"></span>
<span class="score">2 <span>-</span>1</span>
<span class="badge-20 t6826"></span>
<span class="teamName">MUN</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
</ul>
<td class="nextMatchCol hideMed">
</td>
</td>
</tr>
<tr class="expandable" data-filtered-table-row-expander="352">
<td colspan="13">
<a class="expandableTeam" href="/clubs/20/Southampton/overview">
<span class="badge-50 t1189"></span>
<span class="teamName">Southampton</span>
</a>
<div class="expandableFixtures">
<div class="resultWidget">
<div class="label"><strong>Recent Result</strong> - Monday 14 March 2016</div>
<a class="matchAbridged pre" href="/match/13764">
<span class="teamName">SOU</span>
<span class="badge-20 t1189"></span>
<span class="score">2 <span>-</span>1</span>
<span class="badge-20 t6826"></span>
<span class="teamName">MUN</span>
<span class="icn arrow-right"></span>
</a>
</div>
<div class="btnContainer">
<a class="btn-highlight" href="/clubs/20/Southampton/overview" role="btn">Visit <span class="visuallyHidden">Southampton </span>Club Page<span class="icn arrow-right-w"></span></a>
</div>
</div>
<div class="teamPerformanceStandingsArea" style="display:none;">
<header>
<h3 class="subHeader left">Performance Chart</h3>
<a class="btn right" href="/stats/comparison">Compare against another team<span class="icn arrow-right"></span></a>
</header>
<div class="teamPerformanceStandingsContainer"></div>
</div>
</td>
</tr>
<tr class="" data-compseason="39" data-filtered-entry-size="12" data-filtered-table-row="344" data-filtered-table-row-abbr="344" data-filtered-table-row-name="Liverpool" data-filtered-table-row-opta="t7139">
<td class="pos" tabindex="0">
<span class="value">7</span>
</td>
<td class="team" scope="row">
<a href="/clubs/10/Liverpool/overview"><span alt="" class="badge-25 t7139"></span><span class="long">Liverpool</span><span class="short">LIV</span></a>
</td>
<td>22</td>
<td>8</td>
<td>4</td>
<td>10</td>
<td class="hideSmall">26</td>
<td class="hideSmall">37</td>
<td> 
        -11

 </td>
<td class="points">28</td>
<td class="form hideMed">
<ul>
<li class="draw button-tooltip" id="Tooltip" role="tooltip" tabindex="0">D
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13712" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Friday 11 March 2016</span>
<span class="teamName">LIV</span>
<span class="badge-20 t7139"></span>
<span class="score">1 <span>-</span>1</span>
<span class="badge-20 t6826"></span>
<span class="teamName">MUN</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13725" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Sunday 20 March 2016</span>
<span class="teamName">LIV</span>
<span class="badge-20 t7139"></span>
<span class="score">0 <span>-</span>5</span>
<span class="badge-20 t1189"></span>
<span class="teamName">SOU</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13735" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 4 April 2016</span>
<span class="teamName">LEI</span>
<span class="badge-20 t8755"></span>
<span class="score">0 <span>-</span>2</span>
<span class="badge-20 t7139"></span>
<span class="teamName">LIV</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13762" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 25 April 2016</span>
<span class="teamName">LIV</span>
<span class="badge-20 t7139"></span>
<span class="score">2 <span>-</span>1</span>
<span class="badge-20 t6920"></span>
<span class="teamName">NOR</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13769" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Friday 6 May 2016</span>
<span class="teamName">MCI</span>
<span class="badge-20 t1050"></span>
<span class="score">2 <span>-</span>0</span>
<span class="badge-20 t7139"></span>
<span class="teamName">LIV</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
</ul>
<td class="nextMatchCol hideMed">
</td>
</td>
</tr>
<tr class="expandable" data-filtered-table-row-expander="344">
<td colspan="13">
<a class="expandableTeam" href="/clubs/10/Liverpool/overview">
<span class="badge-50 t7139"></span>
<span class="teamName">Liverpool</span>
</a>
<div class="expandableFixtures">
<div class="resultWidget">
<div class="label"><strong>Recent Result</strong> - Friday 11 March 2016</div>
<a class="matchAbridged pre" href="/match/13769">
<span class="teamName">MCI</span>
<span class="badge-20 t1050"></span>
<span class="score">2 <span>-</span>0</span>
<span class="badge-20 t7139"></span>
<span class="teamName">LIV</span>
<span class="icn arrow-right"></span>
</a>
</div>
<div class="btnContainer">
<a class="btn-highlight" href="/clubs/10/Liverpool/overview" role="btn">Visit <span class="visuallyHidden">Liverpool </span>Club Page<span class="icn arrow-right-w"></span></a>
</div>
</div>
<div class="teamPerformanceStandingsArea" style="display:none;">
<header>
<h3 class="subHeader left">Performance Chart</h3>
<a class="btn right" href="/stats/comparison">Compare against another team<span class="icn arrow-right"></span></a>
</header>
<div class="teamPerformanceStandingsContainer"></div>
</div>
</td>
</tr>
<tr class="" data-compseason="39" data-filtered-entry-size="12" data-filtered-table-row="383" data-filtered-table-row-abbr="383" data-filtered-table-row-name="Spurs" data-filtered-table-row-opta="t1175">
<td class="pos" tabindex="0">
<span class="value">8</span>
</td>
<td class="team" scope="row">
<a href="/clubs/21/Tottenham-Hotspur/overview"><span alt="" class="badge-25 t1175"></span><span class="long">Tottenham Hotspur</span><span class="short">TOT</span></a>
</td>
<td>22</td>
<td>7</td>
<td>6</td>
<td>9</td>
<td class="hideSmall">44</td>
<td class="hideSmall">43</td>
<td> 
        +1

 </td>
<td class="points">27</td>
<td class="form hideMed">
<ul>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13714" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Friday 11 March 2016</span>
<span class="teamName">TOT</span>
<span class="badge-20 t1175"></span>
<span class="score">1 <span>-</span>2</span>
<span class="badge-20 t6920"></span>
<span class="teamName">NOR</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13722" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Friday 18 March 2016</span>
<span class="teamName">LEI</span>
<span class="badge-20 t8755"></span>
<span class="score">0 <span>-</span>3</span>
<span class="badge-20 t1175"></span>
<span class="teamName">TOT</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13741" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Wednesday 6 April 2016</span>
<span class="teamName">TOT</span>
<span class="badge-20 t1175"></span>
<span class="score">1 <span>-</span>2</span>
<span class="badge-20 t7138"></span>
<span class="teamName">MID</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13752" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 11 April 2016</span>
<span class="teamName">TOT</span>
<span class="badge-20 t1175"></span>
<span class="score">3 <span>-</span>1</span>
<span class="badge-20 t819"></span>
<span class="teamName">SUN</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13760" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Tuesday 19 April 2016</span>
<span class="teamName">TOT</span>
<span class="badge-20 t1175"></span>
<span class="score">2 <span>-</span>3</span>
<span class="badge-20 t6826"></span>
<span class="teamName">MUN</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
</ul>
<td class="nextMatchCol hideMed">
</td>
</td>
</tr>
<tr class="expandable" data-filtered-table-row-expander="383">
<td colspan="13">
<a class="expandableTeam" href="/clubs/21/Tottenham-Hotspur/overview">
<span class="badge-50 t1175"></span>
<span class="teamName">Tottenham Hotspur</span>
</a>
<div class="expandableFixtures">
<div class="resultWidget">
<div class="label"><strong>Recent Result</strong> - Friday 11 March 2016</div>
<a class="matchAbridged pre" href="/match/13760">
<span class="teamName">TOT</span>
<span class="badge-20 t1175"></span>
<span class="score">2 <span>-</span>3</span>
<span class="badge-20 t6826"></span>
<span class="teamName">MUN</span>
<span class="icn arrow-right"></span>
</a>
</div>
<div class="btnContainer">
<a class="btn-highlight" href="/clubs/21/Tottenham-Hotspur/overview" role="btn">Visit <span class="visuallyHidden">Tottenham Hotspur </span>Club Page<span class="icn arrow-right-w"></span></a>
</div>
</div>
<div class="teamPerformanceStandingsArea" style="display:none;">
<header>
<h3 class="subHeader left">Performance Chart</h3>
<a class="btn right" href="/stats/comparison">Compare against another team<span class="icn arrow-right"></span></a>
</header>
<div class="teamPerformanceStandingsContainer"></div>
</div>
</td>
</tr>
<tr class="" data-compseason="39" data-filtered-entry-size="12" data-filtered-table-row="351" data-filtered-table-row-abbr="351" data-filtered-table-row-name="Reading" data-filtered-table-row-opta="t7608">
<td class="pos" tabindex="0">
<span class="value">9</span>
</td>
<td class="team" scope="row">
<a href="/clubs/40/Reading/overview"><span alt="" class="badge-25 t7608"></span><span class="long">Reading</span><span class="short">RDG</span></a>
</td>
<td>22</td>
<td>7</td>
<td>6</td>
<td>9</td>
<td class="hideSmall">34</td>
<td class="hideSmall">40</td>
<td> 
        -6

 </td>
<td class="points">27</td>
<td class="form hideMed">
<ul>
<li class="draw button-tooltip" id="Tooltip" role="tooltip" tabindex="0">D
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13699" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Thursday 3 March 2016</span>
<span class="teamName">RDG</span>
<span class="badge-20 t7608"></span>
<span class="score">1 <span>-</span>1</span>
<span class="badge-20 t1175"></span>
<span class="teamName">TOT</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13704" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 7 March 2016</span>
<span class="teamName">RDG</span>
<span class="badge-20 t7608"></span>
<span class="score">1 <span>-</span>3</span>
<span class="badge-20 t7140"></span>
<span class="teamName">CHE</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13718" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 14 March 2016</span>
<span class="teamName">EVE</span>
<span class="badge-20 t7592"></span>
<span class="score">0 <span>-</span>2</span>
<span class="badge-20 t7608"></span>
<span class="teamName">RDG</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="draw button-tooltip" id="Tooltip" role="tooltip" tabindex="0">D
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13728" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 21 March 2016</span>
<span class="teamName">NOR</span>
<span class="badge-20 t6920"></span>
<span class="score">4 <span>-</span>4</span>
<span class="badge-20 t7608"></span>
<span class="teamName">RDG</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13751" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 11 April 2016</span>
<span class="teamName">RDG</span>
<span class="badge-20 t7608"></span>
<span class="score">0 <span>-</span>3</span>
<span class="badge-20 t1050"></span>
<span class="teamName">MCI</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
</ul>
<td class="nextMatchCol hideMed">
</td>
</td>
</tr>
<tr class="expandable" data-filtered-table-row-expander="351">
<td colspan="13">
<a class="expandableTeam" href="/clubs/40/Reading/overview">
<span class="badge-50 t7608"></span>
<span class="teamName">Reading</span>
</a>
<div class="expandableFixtures">
<div class="resultWidget">
<div class="label"><strong>Recent Result</strong> - Thursday 3 March 2016</div>
<a class="matchAbridged pre" href="/match/13751">
<span class="teamName">RDG</span>
<span class="badge-20 t7608"></span>
<span class="score">0 <span>-</span>3</span>
<span class="badge-20 t1050"></span>
<span class="teamName">MCI</span>
<span class="icn arrow-right"></span>
</a>
</div>
<div class="btnContainer">
<a class="btn-highlight" href="/clubs/40/Reading/overview" role="btn">Visit <span class="visuallyHidden">Reading </span>Club Page<span class="icn arrow-right-w"></span></a>
</div>
</div>
<div class="teamPerformanceStandingsArea" style="display:none;">
<header>
<h3 class="subHeader left">Performance Chart</h3>
<a class="btn right" href="/stats/comparison">Compare against another team<span class="icn arrow-right"></span></a>
</header>
<div class="teamPerformanceStandingsContainer"></div>
</div>
</td>
</tr>
<tr class="" data-compseason="39" data-filtered-entry-size="12" data-filtered-table-row="343" data-filtered-table-row-abbr="343" data-filtered-table-row-name="Leicester" data-filtered-table-row-opta="t8755">
<td class="pos" tabindex="0">
<span class="value">10</span>
</td>
<td class="team" scope="row">
<a href="/clubs/26/Leicester-City/overview"><span alt="" class="badge-25 t8755"></span><span class="long">Leicester City</span><span class="short">LEI</span></a>
</td>
<td>22</td>
<td>6</td>
<td>3</td>
<td>13</td>
<td class="hideSmall">25</td>
<td class="hideSmall">48</td>
<td> 
        -23

 </td>
<td class="points">21</td>
<td class="form hideMed">
<ul>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13722" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Friday 18 March 2016</span>
<span class="teamName">LEI</span>
<span class="badge-20 t8755"></span>
<span class="score">0 <span>-</span>3</span>
<span class="badge-20 t1175"></span>
<span class="teamName">TOT</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13735" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 4 April 2016</span>
<span class="teamName">LEI</span>
<span class="badge-20 t8755"></span>
<span class="score">0 <span>-</span>2</span>
<span class="badge-20 t7139"></span>
<span class="teamName">LIV</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13748" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 11 April 2016</span>
<span class="teamName">LEI</span>
<span class="badge-20 t8755"></span>
<span class="score">0 <span>-</span>1</span>
<span class="badge-20 t6920"></span>
<span class="teamName">NOR</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13761" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 25 April 2016</span>
<span class="teamName">EVE</span>
<span class="badge-20 t7592"></span>
<span class="score">3 <span>-</span>1</span>
<span class="badge-20 t8755"></span>
<span class="teamName">LEI</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13772" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Thursday 12 May 2016</span>
<span class="teamName">LEI</span>
<span class="badge-20 t8755"></span>
<span class="score">3 <span>-</span>0</span>
<span class="badge-20 t7140"></span>
<span class="teamName">CHE</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
</ul>
<td class="nextMatchCol hideMed">
</td>
</td>
</tr>
<tr class="expandable" data-filtered-table-row-expander="343">
<td colspan="13">
<a class="expandableTeam" href="/clubs/26/Leicester-City/overview">
<span class="badge-50 t8755"></span>
<span class="teamName">Leicester City</span>
</a>
<div class="expandableFixtures">
<div class="resultWidget">
<div class="label"><strong>Recent Result</strong> - Friday 18 March 2016</div>
<a class="matchAbridged pre" href="/match/13772">
<span class="teamName">LEI</span>
<span class="badge-20 t8755"></span>
<span class="score">3 <span>-</span>0</span>
<span class="badge-20 t7140"></span>
<span class="teamName">CHE</span>
<span class="icn arrow-right"></span>
</a>
</div>
<div class="btnContainer">
<a class="btn-highlight" href="/clubs/26/Leicester-City/overview" role="btn">Visit <span class="visuallyHidden">Leicester City </span>Club Page<span class="icn arrow-right-w"></span></a>
</div>
</div>
<div class="teamPerformanceStandingsArea" style="display:none;">
<header>
<h3 class="subHeader left">Performance Chart</h3>
<a class="btn right" href="/stats/comparison">Compare against another team<span class="icn arrow-right"></span></a>
</header>
<div class="teamPerformanceStandingsContainer"></div>
</div>
</td>
</tr>
<tr class="" data-compseason="39" data-filtered-entry-size="12" data-filtered-table-row="345" data-filtered-table-row-abbr="345" data-filtered-table-row-name="Middlesbrough" data-filtered-table-row-opta="t7138">
<td class="pos" tabindex="0">
<span class="value">11</span>
</td>
<td class="team" scope="row">
<a href="/clubs/13/Middlesbrough/overview"><span alt="" class="badge-25 t7138"></span><span class="long">Middlesbrough</span><span class="short">MID</span></a>
</td>
<td>22</td>
<td>5</td>
<td>5</td>
<td>12</td>
<td class="hideSmall">33</td>
<td class="hideSmall">37</td>
<td> 
        -4

 </td>
<td class="points">20</td>
<td class="form hideMed">
<ul>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13727" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 21 March 2016</span>
<span class="teamName">MID</span>
<span class="badge-20 t7138"></span>
<span class="score">0 <span>-</span>1</span>
<span class="badge-20 t819"></span>
<span class="teamName">SUN</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13731" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Friday 1 April 2016</span>
<span class="teamName">MID</span>
<span class="badge-20 t7138"></span>
<span class="score">3 <span>-</span>1</span>
<span class="badge-20 t1050"></span>
<span class="teamName">MCI</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13741" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Wednesday 6 April 2016</span>
<span class="teamName">TOT</span>
<span class="badge-20 t1175"></span>
<span class="score">1 <span>-</span>2</span>
<span class="badge-20 t7138"></span>
<span class="teamName">MID</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13749" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 11 April 2016</span>
<span class="teamName">MUN</span>
<span class="badge-20 t6826"></span>
<span class="score">1 <span>-</span>0</span>
<span class="badge-20 t7138"></span>
<span class="teamName">MID</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13763" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 25 April 2016</span>
<span class="teamName">MID</span>
<span class="badge-20 t7138"></span>
<span class="score">1 <span>-</span>3</span>
<span class="badge-20 t7140"></span>
<span class="teamName">CHE</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
</ul>
<td class="nextMatchCol hideMed">
</td>
</td>
</tr>
<tr class="expandable" data-filtered-table-row-expander="345">
<td colspan="13">
<a class="expandableTeam" href="/clubs/13/Middlesbrough/overview">
<span class="badge-50 t7138"></span>
<span class="teamName">Middlesbrough</span>
</a>
<div class="expandableFixtures">
<div class="resultWidget">
<div class="label"><strong>Recent Result</strong> - Monday 21 March 2016</div>
<a class="matchAbridged pre" href="/match/13763">
<span class="teamName">MID</span>
<span class="badge-20 t7138"></span>
<span class="score">1 <span>-</span>3</span>
<span class="badge-20 t7140"></span>
<span class="teamName">CHE</span>
<span class="icn arrow-right"></span>
</a>
</div>
<div class="btnContainer">
<a class="btn-highlight" href="/clubs/13/Middlesbrough/overview" role="btn">Visit <span class="visuallyHidden">Middlesbrough </span>Club Page<span class="icn arrow-right-w"></span></a>
</div>
</div>
<div class="teamPerformanceStandingsArea" style="display:none;">
<header>
<h3 class="subHeader left">Performance Chart</h3>
<a class="btn right" href="/stats/comparison">Compare against another team<span class="icn arrow-right"></span></a>
</header>
<div class="teamPerformanceStandingsContainer"></div>
</div>
</td>
</tr>
<tr class="" data-compseason="39" data-filtered-entry-size="12" data-filtered-table-row="347" data-filtered-table-row-abbr="347" data-filtered-table-row-name="Norwich" data-filtered-table-row-opta="t6920">
<td class="pos" tabindex="0">
<span class="value">12</span>
</td>
<td class="team" scope="row">
<a href="/clubs/14/Norwich-City/overview"><span alt="" class="badge-25 t6920"></span><span class="long">Norwich City</span><span class="short">NOR</span></a>
</td>
<td>22</td>
<td>5</td>
<td>4</td>
<td>13</td>
<td class="hideSmall">30</td>
<td class="hideSmall">50</td>
<td> 
        -20

 </td>
<td class="points">19</td>
<td class="form hideMed">
<ul>
<li class="draw button-tooltip" id="Tooltip" role="tooltip" tabindex="0">D
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13728" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 21 March 2016</span>
<span class="teamName">NOR</span>
<span class="badge-20 t6920"></span>
<span class="score">4 <span>-</span>4</span>
<span class="badge-20 t7608"></span>
<span class="teamName">RDG</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13737" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 4 April 2016</span>
<span class="teamName">NOR</span>
<span class="badge-20 t6920"></span>
<span class="score">1 <span>-</span>2</span>
<span class="badge-20 t7592"></span>
<span class="teamName">EVE</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13748" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 11 April 2016</span>
<span class="teamName">LEI</span>
<span class="badge-20 t8755"></span>
<span class="score">0 <span>-</span>1</span>
<span class="badge-20 t6920"></span>
<span class="teamName">NOR</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13758" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 18 April 2016</span>
<span class="teamName">SOU</span>
<span class="badge-20 t1189"></span>
<span class="score">3 <span>-</span>2</span>
<span class="badge-20 t6920"></span>
<span class="teamName">NOR</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13762" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 25 April 2016</span>
<span class="teamName">LIV</span>
<span class="badge-20 t7139"></span>
<span class="score">2 <span>-</span>1</span>
<span class="badge-20 t6920"></span>
<span class="teamName">NOR</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
</ul>
<td class="nextMatchCol hideMed">
</td>
</td>
</tr>
<tr class="expandable" data-filtered-table-row-expander="347">
<td colspan="13">
<a class="expandableTeam" href="/clubs/14/Norwich-City/overview">
<span class="badge-50 t6920"></span>
<span class="teamName">Norwich City</span>
</a>
<div class="expandableFixtures">
<div class="resultWidget">
<div class="label"><strong>Recent Result</strong> - Monday 21 March 2016</div>
<a class="matchAbridged pre" href="/match/13762">
<span class="teamName">LIV</span>
<span class="badge-20 t7139"></span>
<span class="score">2 <span>-</span>1</span>
<span class="badge-20 t6920"></span>
<span class="teamName">NOR</span>
<span class="icn arrow-right"></span>
</a>
</div>
<div class="btnContainer">
<a class="btn-highlight" href="/clubs/14/Norwich-City/overview" role="btn">Visit <span class="visuallyHidden">Norwich City </span>Club Page<span class="icn arrow-right-w"></span></a>
</div>
</div>
<div class="teamPerformanceStandingsArea" style="display:none;">
<header>
<h3 class="subHeader left">Performance Chart</h3>
<a class="btn right" href="/stats/comparison">Compare against another team<span class="icn arrow-right"></span></a>
</header>
<div class="teamPerformanceStandingsContainer"></div>
</div>
</td>
</tr>
</tbody>
</table>
</div>, <div class="table wrapper col-12">
<table>
<summary class="visuallyHidden">This table charts the Premier League teams</summary>
<thead>
<tr>
<th class="text-centre" scope="col">
<div class="thFull">Position</div>
<div class="thShort">Pos</div>
</th>
<th class="team" scope="col">Club</th>
<th scope="col">
<div class="thFull">Played</div>
<div class="thShort">Pl</div>
</th>
<th scope="col">
<div class="thFull">Won</div>
<div class="thShort">W</div>
</th>
<th scope="col">
<div class="thFull">Drawn</div>
<div class="thShort">D</div>
</th>
<th scope="col">
<div class="thFull">Lost</div>
<div class="thShort">L</div>
</th>
<th class="hideSmall" scope="col"><abbr title="Goals For">GF</abbr></th>
<th class="hideSmall" scope="col"><abbr title="Goals Against">GA</abbr></th>
<th scope="col"><abbr title="Goal Difference">GD</abbr></th>
<th class="points" scope="col">
<div class="thFull">Points</div>
<div class="thShort">Pts</div>
</th>
<th class="teamForm hideMed" scope="col">Form</th>
<th class="hideMed text-centre" scope="col">Next</th>
</tr>
</thead>
<tbody class="tableBodyContainer">
<tr class="tableDark" data-compseason="39" data-filtered-entry-size="12" data-filtered-table-row="337" data-filtered-table-row-abbr="337" data-filtered-table-row-name="Derby" data-filtered-table-row-opta="t8946">
<td class="pos" tabindex="0">
<span class="value">1</span>
</td>
<td class="team" scope="row">
<a href="/clubs/28/Derby-County/overview"><span alt="" class="badge-25 t8946"></span><span class="long">Derby County</span><span class="short">DER</span></a>
</td>
<td>22</td>
<td>13</td>
<td>3</td>
<td>6</td>
<td class="hideSmall">44</td>
<td class="hideSmall">26</td>
<td> 
        +18

 </td>
<td class="points">42</td>
<td class="form hideMed">
<ul>
<li class="draw button-tooltip" id="Tooltip" role="tooltip" tabindex="0">D
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13689" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 22 February 2016</span>
<span class="teamName">DER</span>
<span class="badge-20 t8946"></span>
<span class="score">2 <span>-</span>2</span>
<span class="badge-20 t8951"></span>
<span class="teamName">BHA</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13706" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 7 March 2016</span>
<span class="teamName">SWA</span>
<span class="badge-20 t8950"></span>
<span class="score">2 <span>-</span>1</span>
<span class="badge-20 t8946"></span>
<span class="teamName">DER</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13711" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Friday 11 March 2016</span>
<span class="teamName">DER</span>
<span class="badge-20 t8946"></span>
<span class="score">2 <span>-</span>0</span>
<span class="badge-20 t7595"></span>
<span class="teamName">WBA</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13734" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 4 April 2016</span>
<span class="teamName">FUL</span>
<span class="badge-20 t6912"></span>
<span class="score">0 <span>-</span>1</span>
<span class="badge-20 t8946"></span>
<span class="teamName">DER</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13746" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 11 April 2016</span>
<span class="teamName">DER</span>
<span class="badge-20 t8946"></span>
<span class="score">1 <span>-</span>2</span>
<span class="badge-20 t7594"></span>
<span class="teamName">ARS</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
</ul>
<td class="nextMatchCol hideMed">
</td>
</td>
</tr>
<tr class="expandable" data-filtered-table-row-expander="337">
<td colspan="13">
<a class="expandableTeam" href="/clubs/28/Derby-County/overview">
<span class="badge-50 t8946"></span>
<span class="teamName">Derby County</span>
</a>
<div class="expandableFixtures">
<div class="resultWidget">
<div class="label"><strong>Recent Result</strong> - Monday 22 February 2016</div>
<a class="matchAbridged pre" href="/match/13746">
<span class="teamName">DER</span>
<span class="badge-20 t8946"></span>
<span class="score">1 <span>-</span>2</span>
<span class="badge-20 t7594"></span>
<span class="teamName">ARS</span>
<span class="icn arrow-right"></span>
</a>
</div>
<div class="btnContainer">
<a class="btn-highlight" href="/clubs/28/Derby-County/overview" role="btn">Visit <span class="visuallyHidden">Derby County </span>Club Page<span class="icn arrow-right-w"></span></a>
</div>
</div>
<div class="teamPerformanceStandingsArea" style="display:none;">
<header>
<h3 class="subHeader left">Performance Chart</h3>
<a class="btn right" href="/stats/comparison">Compare against another team<span class="icn arrow-right"></span></a>
</header>
<div class="teamPerformanceStandingsContainer"></div>
</div>
</td>
</tr>
<tr class="" data-compseason="39" data-filtered-entry-size="12" data-filtered-table-row="385" data-filtered-table-row-abbr="385" data-filtered-table-row-name="Arsenal" data-filtered-table-row-opta="t7594">
<td class="pos" tabindex="0">
<span class="value">2</span>
</td>
<td class="team" scope="row">
<a href="/clubs/1/Arsenal/overview"><span alt="" class="badge-25 t7594"></span><span class="long">Arsenal</span><span class="short">ARS</span></a>
</td>
<td>22</td>
<td>12</td>
<td>4</td>
<td>6</td>
<td class="hideSmall">40</td>
<td class="hideSmall">25</td>
<td> 
        +15

 </td>
<td class="points">40</td>
<td class="form hideMed">
<ul>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13746" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 11 April 2016</span>
<span class="teamName">DER</span>
<span class="badge-20 t8946"></span>
<span class="score">1 <span>-</span>2</span>
<span class="badge-20 t7594"></span>
<span class="teamName">ARS</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13754" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Thursday 14 April 2016</span>
<span class="teamName">SWA</span>
<span class="badge-20 t8950"></span>
<span class="score">3 <span>-</span>1</span>
<span class="badge-20 t7594"></span>
<span class="teamName">ARS</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13755" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 18 April 2016</span>
<span class="teamName">ARS</span>
<span class="badge-20 t7594"></span>
<span class="score">1 <span>-</span>2</span>
<span class="badge-20 t7595"></span>
<span class="teamName">WBA</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13767" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Tuesday 3 May 2016</span>
<span class="teamName">ARS</span>
<span class="badge-20 t7594"></span>
<span class="score">2 <span>-</span>1</span>
<span class="badge-20 t7590"></span>
<span class="teamName">BLB</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13771" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Tuesday 10 May 2016</span>
<span class="teamName">ARS</span>
<span class="badge-20 t7594"></span>
<span class="score">3 <span>-</span>1</span>
<span class="badge-20 t7591"></span>
<span class="teamName">AVL</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
</ul>
<td class="nextMatchCol hideMed">
</td>
</td>
</tr>
<tr class="expandable" data-filtered-table-row-expander="385">
<td colspan="13">
<a class="expandableTeam" href="/clubs/1/Arsenal/overview">
<span class="badge-50 t7594"></span>
<span class="teamName">Arsenal</span>
</a>
<div class="expandableFixtures">
<div class="resultWidget">
<div class="label"><strong>Recent Result</strong> - Monday 11 April 2016</div>
<a class="matchAbridged pre" href="/match/13771">
<span class="teamName">ARS</span>
<span class="badge-20 t7594"></span>
<span class="score">3 <span>-</span>1</span>
<span class="badge-20 t7591"></span>
<span class="teamName">AVL</span>
<span class="icn arrow-right"></span>
</a>
</div>
<div class="btnContainer">
<a class="btn-highlight" href="/clubs/1/Arsenal/overview" role="btn">Visit <span class="visuallyHidden">Arsenal </span>Club Page<span class="icn arrow-right-w"></span></a>
</div>
</div>
<div class="teamPerformanceStandingsArea" style="display:none;">
<header>
<h3 class="subHeader left">Performance Chart</h3>
<a class="btn right" href="/stats/comparison">Compare against another team<span class="icn arrow-right"></span></a>
</header>
<div class="teamPerformanceStandingsContainer"></div>
</div>
</td>
</tr>
<tr class="" data-compseason="39" data-filtered-entry-size="12" data-filtered-table-row="356" data-filtered-table-row-abbr="356" data-filtered-table-row-name="Swansea" data-filtered-table-row-opta="t8950">
<td class="pos" tabindex="0">
<span class="value">3</span>
</td>
<td class="team" scope="row">
<a href="/clubs/45/Swansea-City/overview"><span alt="" class="badge-25 t8950"></span><span class="long">Swansea City</span><span class="short">SWA</span></a>
</td>
<td>22</td>
<td>12</td>
<td>3</td>
<td>7</td>
<td class="hideSmall">42</td>
<td class="hideSmall">24</td>
<td> 
        +18

 </td>
<td class="points">39</td>
<td class="form hideMed">
<ul>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13738" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 4 April 2016</span>
<span class="teamName">SWA</span>
<span class="badge-20 t8950"></span>
<span class="score">5 <span>-</span>3</span>
<span class="badge-20 t7609"></span>
<span class="teamName">NEW</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13743" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 9 April 2016</span>
<span class="teamName">STK</span>
<span class="badge-20 t6927"></span>
<span class="score">1 <span>-</span>2</span>
<span class="badge-20 t8950"></span>
<span class="teamName">SWA</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13754" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Thursday 14 April 2016</span>
<span class="teamName">SWA</span>
<span class="badge-20 t8950"></span>
<span class="score">3 <span>-</span>1</span>
<span class="badge-20 t7594"></span>
<span class="teamName">ARS</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13759" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 18 April 2016</span>
<span class="teamName">SWA</span>
<span class="badge-20 t8950"></span>
<span class="score">3 <span>-</span>0</span>
<span class="badge-20 t6912"></span>
<span class="teamName">FUL</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13765" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 25 April 2016</span>
<span class="teamName">SWA</span>
<span class="badge-20 t8950"></span>
<span class="score">1 <span>-</span>2</span>
<span class="badge-20 t7591"></span>
<span class="teamName">AVL</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
</ul>
<td class="nextMatchCol hideMed">
</td>
</td>
</tr>
<tr class="expandable" data-filtered-table-row-expander="356">
<td colspan="13">
<a class="expandableTeam" href="/clubs/45/Swansea-City/overview">
<span class="badge-50 t8950"></span>
<span class="teamName">Swansea City</span>
</a>
<div class="expandableFixtures">
<div class="resultWidget">
<div class="label"><strong>Recent Result</strong> - Monday 4 April 2016</div>
<a class="matchAbridged pre" href="/match/13765">
<span class="teamName">SWA</span>
<span class="badge-20 t8950"></span>
<span class="score">1 <span>-</span>2</span>
<span class="badge-20 t7591"></span>
<span class="teamName">AVL</span>
<span class="icn arrow-right"></span>
</a>
</div>
<div class="btnContainer">
<a class="btn-highlight" href="/clubs/45/Swansea-City/overview" role="btn">Visit <span class="visuallyHidden">Swansea City </span>Club Page<span class="icn arrow-right-w"></span></a>
</div>
</div>
<div class="teamPerformanceStandingsArea" style="display:none;">
<header>
<h3 class="subHeader left">Performance Chart</h3>
<a class="btn right" href="/stats/comparison">Compare against another team<span class="icn arrow-right"></span></a>
</header>
<div class="teamPerformanceStandingsContainer"></div>
</div>
</td>
</tr>
<tr class="" data-compseason="39" data-filtered-entry-size="12" data-filtered-table-row="386" data-filtered-table-row-abbr="386" data-filtered-table-row-name="Aston Villa" data-filtered-table-row-opta="t7591">
<td class="pos" tabindex="0">
<span class="value">4</span>
</td>
<td class="team" scope="row">
<a href="/clubs/2/Aston-Villa/overview"><span alt="" class="badge-25 t7591"></span><span class="long">Aston Villa</span><span class="short">AVL</span></a>
</td>
<td>22</td>
<td>11</td>
<td>6</td>
<td>5</td>
<td class="hideSmall">28</td>
<td class="hideSmall">27</td>
<td> 
        +1

 </td>
<td class="points">39</td>
<td class="form hideMed">
<ul>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13739" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 4 April 2016</span>
<span class="teamName">WBA</span>
<span class="badge-20 t7595"></span>
<span class="score">1 <span>-</span>0</span>
<span class="badge-20 t7591"></span>
<span class="teamName">AVL</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13744" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 11 April 2016</span>
<span class="teamName">AVL</span>
<span class="badge-20 t7591"></span>
<span class="score">3 <span>-</span>2</span>
<span class="badge-20 t7238"></span>
<span class="teamName">WHU</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="draw button-tooltip" id="Tooltip" role="tooltip" tabindex="0">D
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13756" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 18 April 2016</span>
<span class="teamName">BLB</span>
<span class="badge-20 t7590"></span>
<span class="score">2 <span>-</span>2</span>
<span class="badge-20 t7591"></span>
<span class="teamName">AVL</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13765" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 25 April 2016</span>
<span class="teamName">SWA</span>
<span class="badge-20 t8950"></span>
<span class="score">1 <span>-</span>2</span>
<span class="badge-20 t7591"></span>
<span class="teamName">AVL</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13771" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Tuesday 10 May 2016</span>
<span class="teamName">ARS</span>
<span class="badge-20 t7594"></span>
<span class="score">3 <span>-</span>1</span>
<span class="badge-20 t7591"></span>
<span class="teamName">AVL</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
</ul>
<td class="nextMatchCol hideMed">
</td>
</td>
</tr>
<tr class="expandable" data-filtered-table-row-expander="386">
<td colspan="13">
<a class="expandableTeam" href="/clubs/2/Aston-Villa/overview">
<span class="badge-50 t7591"></span>
<span class="teamName">Aston Villa</span>
</a>
<div class="expandableFixtures">
<div class="resultWidget">
<div class="label"><strong>Recent Result</strong> - Monday 4 April 2016</div>
<a class="matchAbridged pre" href="/match/13771">
<span class="teamName">ARS</span>
<span class="badge-20 t7594"></span>
<span class="score">3 <span>-</span>1</span>
<span class="badge-20 t7591"></span>
<span class="teamName">AVL</span>
<span class="icn arrow-right"></span>
</a>
</div>
<div class="btnContainer">
<a class="btn-highlight" href="/clubs/2/Aston-Villa/overview" role="btn">Visit <span class="visuallyHidden">Aston Villa </span>Club Page<span class="icn arrow-right-w"></span></a>
</div>
</div>
<div class="teamPerformanceStandingsArea" style="display:none;">
<header>
<h3 class="subHeader left">Performance Chart</h3>
<a class="btn right" href="/stats/comparison">Compare against another team<span class="icn arrow-right"></span></a>
</header>
<div class="teamPerformanceStandingsContainer"></div>
</div>
</td>
</tr>
<tr class="" data-compseason="39" data-filtered-entry-size="12" data-filtered-table-row="332" data-filtered-table-row-abbr="332" data-filtered-table-row-name="Blackburn" data-filtered-table-row-opta="t7590">
<td class="pos" tabindex="0">
<span class="value">5</span>
</td>
<td class="team" scope="row">
<a href="/clubs/3/Blackburn-Rovers/overview"><span alt="" class="badge-25 t7590"></span><span class="long">Blackburn Rovers</span><span class="short">BLB</span></a>
</td>
<td>22</td>
<td>10</td>
<td>4</td>
<td>8</td>
<td class="hideSmall">29</td>
<td class="hideSmall">33</td>
<td> 
        -4

 </td>
<td class="points">34</td>
<td class="form hideMed">
<ul>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13730" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Friday 1 April 2016</span>
<span class="teamName">BLB</span>
<span class="badge-20 t7590"></span>
<span class="score">1 <span>-</span>0</span>
<span class="badge-20 t7594"></span>
<span class="teamName">ARS</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13733" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 4 April 2016</span>
<span class="teamName">BHA</span>
<span class="badge-20 t8951"></span>
<span class="score">0 <span>-</span>1</span>
<span class="badge-20 t7590"></span>
<span class="teamName">BLB</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13745" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 11 April 2016</span>
<span class="teamName">BLB</span>
<span class="badge-20 t7590"></span>
<span class="score">2 <span>-</span>1</span>
<span class="badge-20 t7595"></span>
<span class="teamName">WBA</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="draw button-tooltip" id="Tooltip" role="tooltip" tabindex="0">D
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13756" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 18 April 2016</span>
<span class="teamName">BLB</span>
<span class="badge-20 t7590"></span>
<span class="score">2 <span>-</span>2</span>
<span class="badge-20 t7591"></span>
<span class="teamName">AVL</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13767" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Tuesday 3 May 2016</span>
<span class="teamName">ARS</span>
<span class="badge-20 t7594"></span>
<span class="score">2 <span>-</span>1</span>
<span class="badge-20 t7590"></span>
<span class="teamName">BLB</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
</ul>
<td class="nextMatchCol hideMed">
</td>
</td>
</tr>
<tr class="expandable" data-filtered-table-row-expander="332">
<td colspan="13">
<a class="expandableTeam" href="/clubs/3/Blackburn-Rovers/overview">
<span class="badge-50 t7590"></span>
<span class="teamName">Blackburn Rovers</span>
</a>
<div class="expandableFixtures">
<div class="resultWidget">
<div class="label"><strong>Recent Result</strong> - Friday 1 April 2016</div>
<a class="matchAbridged pre" href="/match/13767">
<span class="teamName">ARS</span>
<span class="badge-20 t7594"></span>
<span class="score">2 <span>-</span>1</span>
<span class="badge-20 t7590"></span>
<span class="teamName">BLB</span>
<span class="icn arrow-right"></span>
</a>
</div>
<div class="btnContainer">
<a class="btn-highlight" href="/clubs/3/Blackburn-Rovers/overview" role="btn">Visit <span class="visuallyHidden">Blackburn Rovers </span>Club Page<span class="icn arrow-right-w"></span></a>
</div>
</div>
<div class="teamPerformanceStandingsArea" style="display:none;">
<header>
<h3 class="subHeader left">Performance Chart</h3>
<a class="btn right" href="/stats/comparison">Compare against another team<span class="icn arrow-right"></span></a>
</header>
<div class="teamPerformanceStandingsContainer"></div>
</div>
</td>
</tr>
<tr class="" data-compseason="39" data-filtered-entry-size="12" data-filtered-table-row="357" data-filtered-table-row-abbr="357" data-filtered-table-row-name="West Brom" data-filtered-table-row-opta="t7595">
<td class="pos" tabindex="0">
<span class="value">6</span>
</td>
<td class="team" scope="row">
<a href="/clubs/36/West-Bromwich-Albion/overview"><span alt="" class="badge-25 t7595"></span><span class="long">West Bromwich Albion</span><span class="short">WBA</span></a>
</td>
<td>22</td>
<td>8</td>
<td>9</td>
<td>5</td>
<td class="hideSmall">24</td>
<td class="hideSmall">20</td>
<td> 
        +4

 </td>
<td class="points">33</td>
<td class="form hideMed">
<ul>
<li class="draw button-tooltip" id="Tooltip" role="tooltip" tabindex="0">D
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13708" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Tuesday 8 March 2016</span>
<span class="teamName">WBA</span>
<span class="badge-20 t7595"></span>
<span class="score">0 <span>-</span>0</span>
<span class="badge-20 t7136"></span>
<span class="teamName">WOL</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13711" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Friday 11 March 2016</span>
<span class="teamName">DER</span>
<span class="badge-20 t8946"></span>
<span class="score">2 <span>-</span>0</span>
<span class="badge-20 t7595"></span>
<span class="teamName">WBA</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13739" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 4 April 2016</span>
<span class="teamName">WBA</span>
<span class="badge-20 t7595"></span>
<span class="score">1 <span>-</span>0</span>
<span class="badge-20 t7591"></span>
<span class="teamName">AVL</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13745" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 11 April 2016</span>
<span class="teamName">BLB</span>
<span class="badge-20 t7590"></span>
<span class="score">2 <span>-</span>1</span>
<span class="badge-20 t7595"></span>
<span class="teamName">WBA</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13755" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 18 April 2016</span>
<span class="teamName">ARS</span>
<span class="badge-20 t7594"></span>
<span class="score">1 <span>-</span>2</span>
<span class="badge-20 t7595"></span>
<span class="teamName">WBA</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
</ul>
<td class="nextMatchCol hideMed">
</td>
</td>
</tr>
<tr class="expandable" data-filtered-table-row-expander="357">
<td colspan="13">
<a class="expandableTeam" href="/clubs/36/West-Bromwich-Albion/overview">
<span class="badge-50 t7595"></span>
<span class="teamName">West Bromwich Albion</span>
</a>
<div class="expandableFixtures">
<div class="resultWidget">
<div class="label"><strong>Recent Result</strong> - Tuesday 8 March 2016</div>
<a class="matchAbridged pre" href="/match/13755">
<span class="teamName">ARS</span>
<span class="badge-20 t7594"></span>
<span class="score">1 <span>-</span>2</span>
<span class="badge-20 t7595"></span>
<span class="teamName">WBA</span>
<span class="icn arrow-right"></span>
</a>
</div>
<div class="btnContainer">
<a class="btn-highlight" href="/clubs/36/West-Bromwich-Albion/overview" role="btn">Visit <span class="visuallyHidden">West Bromwich Albion </span>Club Page<span class="icn arrow-right-w"></span></a>
</div>
</div>
<div class="teamPerformanceStandingsArea" style="display:none;">
<header>
<h3 class="subHeader left">Performance Chart</h3>
<a class="btn right" href="/stats/comparison">Compare against another team<span class="icn arrow-right"></span></a>
</header>
<div class="teamPerformanceStandingsContainer"></div>
</div>
</td>
</tr>
<tr class="" data-compseason="39" data-filtered-entry-size="12" data-filtered-table-row="358" data-filtered-table-row-abbr="358" data-filtered-table-row-name="West Ham" data-filtered-table-row-opta="t7238">
<td class="pos" tabindex="0">
<span class="value">7</span>
</td>
<td class="team" scope="row">
<a href="/clubs/25/West-Ham-United/overview"><span alt="" class="badge-25 t7238"></span><span class="long">West Ham United</span><span class="short">WHU</span></a>
</td>
<td>22</td>
<td>9</td>
<td>5</td>
<td>8</td>
<td class="hideSmall">37</td>
<td class="hideSmall">34</td>
<td> 
        +3

 </td>
<td class="points">32</td>
<td class="form hideMed">
<ul>
<li class="draw button-tooltip" id="Tooltip" role="tooltip" tabindex="0">D
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13692" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 22 February 2016</span>
<span class="teamName">WOL</span>
<span class="badge-20 t7136"></span>
<span class="score">1 <span>-</span>1</span>
<span class="badge-20 t7238"></span>
<span class="teamName">WHU</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="draw button-tooltip" id="Tooltip" role="tooltip" tabindex="0">D
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13707" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 7 March 2016</span>
<span class="teamName">WHU</span>
<span class="badge-20 t7238"></span>
<span class="score">1 <span>-</span>1</span>
<span class="badge-20 t7590"></span>
<span class="teamName">BLB</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13713" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Friday 11 March 2016</span>
<span class="teamName">NEW</span>
<span class="badge-20 t7609"></span>
<span class="score">1 <span>-</span>4</span>
<span class="badge-20 t7238"></span>
<span class="teamName">WHU</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13740" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 4 April 2016</span>
<span class="teamName">WHU</span>
<span class="badge-20 t7238"></span>
<span class="score">1 <span>-</span>0</span>
<span class="badge-20 t6927"></span>
<span class="teamName">STK</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13744" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 11 April 2016</span>
<span class="teamName">AVL</span>
<span class="badge-20 t7591"></span>
<span class="score">3 <span>-</span>2</span>
<span class="badge-20 t7238"></span>
<span class="teamName">WHU</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
</ul>
<td class="nextMatchCol hideMed">
</td>
</td>
</tr>
<tr class="expandable" data-filtered-table-row-expander="358">
<td colspan="13">
<a class="expandableTeam" href="/clubs/25/West-Ham-United/overview">
<span class="badge-50 t7238"></span>
<span class="teamName">West Ham United</span>
</a>
<div class="expandableFixtures">
<div class="resultWidget">
<div class="label"><strong>Recent Result</strong> - Monday 22 February 2016</div>
<a class="matchAbridged pre" href="/match/13744">
<span class="teamName">AVL</span>
<span class="badge-20 t7591"></span>
<span class="score">3 <span>-</span>2</span>
<span class="badge-20 t7238"></span>
<span class="teamName">WHU</span>
<span class="icn arrow-right"></span>
</a>
</div>
<div class="btnContainer">
<a class="btn-highlight" href="/clubs/25/West-Ham-United/overview" role="btn">Visit <span class="visuallyHidden">West Ham United </span>Club Page<span class="icn arrow-right-w"></span></a>
</div>
</div>
<div class="teamPerformanceStandingsArea" style="display:none;">
<header>
<h3 class="subHeader left">Performance Chart</h3>
<a class="btn right" href="/stats/comparison">Compare against another team<span class="icn arrow-right"></span></a>
</header>
<div class="teamPerformanceStandingsContainer"></div>
</div>
</td>
</tr>
<tr class="" data-compseason="39" data-filtered-entry-size="12" data-filtered-table-row="354" data-filtered-table-row-abbr="354" data-filtered-table-row-name="Stoke City" data-filtered-table-row-opta="t6927">
<td class="pos" tabindex="0">
<span class="value">8</span>
</td>
<td class="team" scope="row">
<a href="/clubs/42/Stoke-City/overview"><span alt="" class="badge-25 t6927"></span><span class="long">Stoke City</span><span class="short">STK</span></a>
</td>
<td>22</td>
<td>10</td>
<td>2</td>
<td>10</td>
<td class="hideSmall">24</td>
<td class="hideSmall">24</td>
<td> 
        0

 </td>
<td class="points">32</td>
<td class="form hideMed">
<ul>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13686" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 20 February 2016</span>
<span class="teamName">STK</span>
<span class="badge-20 t6927"></span>
<span class="score">2 <span>-</span>1</span>
<span class="badge-20 t7595"></span>
<span class="teamName">WBA</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="draw button-tooltip" id="Tooltip" role="tooltip" tabindex="0">D
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13698" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Wednesday 2 March 2016</span>
<span class="teamName">FUL</span>
<span class="badge-20 t6912"></span>
<span class="score">1 <span>-</span>1</span>
<span class="badge-20 t6927"></span>
<span class="teamName">STK</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13724" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 19 March 2016</span>
<span class="teamName">STK</span>
<span class="badge-20 t6927"></span>
<span class="score">1 <span>-</span>0</span>
<span class="badge-20 t8951"></span>
<span class="teamName">BHA</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13740" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 4 April 2016</span>
<span class="teamName">WHU</span>
<span class="badge-20 t7238"></span>
<span class="score">1 <span>-</span>0</span>
<span class="badge-20 t6927"></span>
<span class="teamName">STK</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13743" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 9 April 2016</span>
<span class="teamName">STK</span>
<span class="badge-20 t6927"></span>
<span class="score">1 <span>-</span>2</span>
<span class="badge-20 t8950"></span>
<span class="teamName">SWA</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
</ul>
<td class="nextMatchCol hideMed">
</td>
</td>
</tr>
<tr class="expandable" data-filtered-table-row-expander="354">
<td colspan="13">
<a class="expandableTeam" href="/clubs/42/Stoke-City/overview">
<span class="badge-50 t6927"></span>
<span class="teamName">Stoke City</span>
</a>
<div class="expandableFixtures">
<div class="resultWidget">
<div class="label"><strong>Recent Result</strong> - Saturday 20 February 2016</div>
<a class="matchAbridged pre" href="/match/13743">
<span class="teamName">STK</span>
<span class="badge-20 t6927"></span>
<span class="score">1 <span>-</span>2</span>
<span class="badge-20 t8950"></span>
<span class="teamName">SWA</span>
<span class="icn arrow-right"></span>
</a>
</div>
<div class="btnContainer">
<a class="btn-highlight" href="/clubs/42/Stoke-City/overview" role="btn">Visit <span class="visuallyHidden">Stoke City </span>Club Page<span class="icn arrow-right-w"></span></a>
</div>
</div>
<div class="teamPerformanceStandingsArea" style="display:none;">
<header>
<h3 class="subHeader left">Performance Chart</h3>
<a class="btn right" href="/stats/comparison">Compare against another team<span class="icn arrow-right"></span></a>
</header>
<div class="teamPerformanceStandingsContainer"></div>
</div>
</td>
</tr>
<tr class="" data-compseason="39" data-filtered-entry-size="12" data-filtered-table-row="341" data-filtered-table-row-abbr="341" data-filtered-table-row-name="Fulham" data-filtered-table-row-opta="t6912">
<td class="pos" tabindex="0">
<span class="value">9</span>
</td>
<td class="team" scope="row">
<a href="/clubs/34/Fulham/overview"><span alt="" class="badge-25 t6912"></span><span class="long">Fulham</span><span class="short">FUL</span></a>
</td>
<td>22</td>
<td>8</td>
<td>5</td>
<td>9</td>
<td class="hideSmall">26</td>
<td class="hideSmall">29</td>
<td> 
        -3

 </td>
<td class="points">29</td>
<td class="form hideMed">
<ul>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13709" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Wednesday 9 March 2016</span>
<span class="teamName">FUL</span>
<span class="badge-20 t6912"></span>
<span class="score">0 <span>-</span>3</span>
<span class="badge-20 t7594"></span>
<span class="teamName">ARS</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13717" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 14 March 2016</span>
<span class="teamName">BLB</span>
<span class="badge-20 t7590"></span>
<span class="score">0 <span>-</span>2</span>
<span class="badge-20 t6912"></span>
<span class="teamName">FUL</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13734" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 4 April 2016</span>
<span class="teamName">FUL</span>
<span class="badge-20 t6912"></span>
<span class="score">0 <span>-</span>1</span>
<span class="badge-20 t8946"></span>
<span class="teamName">DER</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13753" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Wednesday 13 April 2016</span>
<span class="teamName">WOL</span>
<span class="badge-20 t7136"></span>
<span class="score">0 <span>-</span>3</span>
<span class="badge-20 t6912"></span>
<span class="teamName">FUL</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13759" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 18 April 2016</span>
<span class="teamName">SWA</span>
<span class="badge-20 t8950"></span>
<span class="score">3 <span>-</span>0</span>
<span class="badge-20 t6912"></span>
<span class="teamName">FUL</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
</ul>
<td class="nextMatchCol hideMed">
</td>
</td>
</tr>
<tr class="expandable" data-filtered-table-row-expander="341">
<td colspan="13">
<a class="expandableTeam" href="/clubs/34/Fulham/overview">
<span class="badge-50 t6912"></span>
<span class="teamName">Fulham</span>
</a>
<div class="expandableFixtures">
<div class="resultWidget">
<div class="label"><strong>Recent Result</strong> - Wednesday 9 March 2016</div>
<a class="matchAbridged pre" href="/match/13759">
<span class="teamName">SWA</span>
<span class="badge-20 t8950"></span>
<span class="score">3 <span>-</span>0</span>
<span class="badge-20 t6912"></span>
<span class="teamName">FUL</span>
<span class="icn arrow-right"></span>
</a>
</div>
<div class="btnContainer">
<a class="btn-highlight" href="/clubs/34/Fulham/overview" role="btn">Visit <span class="visuallyHidden">Fulham </span>Club Page<span class="icn arrow-right-w"></span></a>
</div>
</div>
<div class="teamPerformanceStandingsArea" style="display:none;">
<header>
<h3 class="subHeader left">Performance Chart</h3>
<a class="btn right" href="/stats/comparison">Compare against another team<span class="icn arrow-right"></span></a>
</header>
<div class="teamPerformanceStandingsContainer"></div>
</div>
</td>
</tr>
<tr class="" data-compseason="39" data-filtered-entry-size="12" data-filtered-table-row="346" data-filtered-table-row-abbr="346" data-filtered-table-row-name="Newcastle" data-filtered-table-row-opta="t7609">
<td class="pos" tabindex="0">
<span class="value">10</span>
</td>
<td class="team" scope="row">
<a href="/clubs/23/Newcastle-United/overview"><span alt="" class="badge-25 t7609"></span><span class="long">Newcastle United</span><span class="short">NEW</span></a>
</td>
<td>22</td>
<td>4</td>
<td>6</td>
<td>12</td>
<td class="hideSmall">30</td>
<td class="hideSmall">48</td>
<td> 
        -18

 </td>
<td class="points">18</td>
<td class="form hideMed">
<ul>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13713" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Friday 11 March 2016</span>
<span class="teamName">NEW</span>
<span class="badge-20 t7609"></span>
<span class="score">1 <span>-</span>4</span>
<span class="badge-20 t7238"></span>
<span class="teamName">WHU</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="draw button-tooltip" id="Tooltip" role="tooltip" tabindex="0">D
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13729" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Wednesday 23 March 2016</span>
<span class="teamName">BHA</span>
<span class="badge-20 t8951"></span>
<span class="score">1 <span>-</span>1</span>
<span class="badge-20 t7609"></span>
<span class="teamName">NEW</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13738" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 4 April 2016</span>
<span class="teamName">SWA</span>
<span class="badge-20 t8950"></span>
<span class="score">5 <span>-</span>3</span>
<span class="badge-20 t7609"></span>
<span class="teamName">NEW</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13742" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Friday 8 April 2016</span>
<span class="teamName">ARS</span>
<span class="badge-20 t7594"></span>
<span class="score">3 <span>-</span>1</span>
<span class="badge-20 t7609"></span>
<span class="teamName">NEW</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13750" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 11 April 2016</span>
<span class="teamName">NEW</span>
<span class="badge-20 t7609"></span>
<span class="score">1 <span>-</span>4</span>
<span class="badge-20 t8951"></span>
<span class="teamName">BHA</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
</ul>
<td class="nextMatchCol hideMed">
</td>
</td>
</tr>
<tr class="expandable" data-filtered-table-row-expander="346">
<td colspan="13">
<a class="expandableTeam" href="/clubs/23/Newcastle-United/overview">
<span class="badge-50 t7609"></span>
<span class="teamName">Newcastle United</span>
</a>
<div class="expandableFixtures">
<div class="resultWidget">
<div class="label"><strong>Recent Result</strong> - Friday 11 March 2016</div>
<a class="matchAbridged pre" href="/match/13750">
<span class="teamName">NEW</span>
<span class="badge-20 t7609"></span>
<span class="score">1 <span>-</span>4</span>
<span class="badge-20 t8951"></span>
<span class="teamName">BHA</span>
<span class="icn arrow-right"></span>
</a>
</div>
<div class="btnContainer">
<a class="btn-highlight" href="/clubs/23/Newcastle-United/overview" role="btn">Visit <span class="visuallyHidden">Newcastle United </span>Club Page<span class="icn arrow-right-w"></span></a>
</div>
</div>
<div class="teamPerformanceStandingsArea" style="display:none;">
<header>
<h3 class="subHeader left">Performance Chart</h3>
<a class="btn right" href="/stats/comparison">Compare against another team<span class="icn arrow-right"></span></a>
</header>
<div class="teamPerformanceStandingsContainer"></div>
</div>
</td>
</tr>
<tr class="" data-compseason="39" data-filtered-entry-size="12" data-filtered-table-row="334" data-filtered-table-row-abbr="334" data-filtered-table-row-name="Brighton" data-filtered-table-row-opta="t8951">
<td class="pos" tabindex="0">
<span class="value">11</span>
</td>
<td class="team" scope="row">
<a href="/clubs/131/Brighton-and-Hove-Albion/overview"><span alt="" class="badge-25 t8951"></span><span class="long">Brighton and Hove Albion</span><span class="short">BHA</span></a>
</td>
<td>22</td>
<td>2</td>
<td>8</td>
<td>12</td>
<td class="hideSmall">17</td>
<td class="hideSmall">36</td>
<td> 
        -19

 </td>
<td class="points">14</td>
<td class="form hideMed">
<ul>
<li class="draw button-tooltip" id="Tooltip" role="tooltip" tabindex="0">D
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13701" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 7 March 2016</span>
<span class="teamName">BHA</span>
<span class="badge-20 t8951"></span>
<span class="score">1 <span>-</span>1</span>
<span class="badge-20 t7591"></span>
<span class="teamName">AVL</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13724" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 19 March 2016</span>
<span class="teamName">STK</span>
<span class="badge-20 t6927"></span>
<span class="score">1 <span>-</span>0</span>
<span class="badge-20 t8951"></span>
<span class="teamName">BHA</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="draw button-tooltip" id="Tooltip" role="tooltip" tabindex="0">D
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13729" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Wednesday 23 March 2016</span>
<span class="teamName">BHA</span>
<span class="badge-20 t8951"></span>
<span class="score">1 <span>-</span>1</span>
<span class="badge-20 t7609"></span>
<span class="teamName">NEW</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13733" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 4 April 2016</span>
<span class="teamName">BHA</span>
<span class="badge-20 t8951"></span>
<span class="score">0 <span>-</span>1</span>
<span class="badge-20 t7590"></span>
<span class="teamName">BLB</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13750" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 11 April 2016</span>
<span class="teamName">NEW</span>
<span class="badge-20 t7609"></span>
<span class="score">1 <span>-</span>4</span>
<span class="badge-20 t8951"></span>
<span class="teamName">BHA</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
</ul>
<td class="nextMatchCol hideMed">
</td>
</td>
</tr>
<tr class="expandable" data-filtered-table-row-expander="334">
<td colspan="13">
<a class="expandableTeam" href="/clubs/131/Brighton-and-Hove-Albion/overview">
<span class="badge-50 t8951"></span>
<span class="teamName">Brighton and Hove Albion</span>
</a>
<div class="expandableFixtures">
<div class="resultWidget">
<div class="label"><strong>Recent Result</strong> - Monday 7 March 2016</div>
<a class="matchAbridged pre" href="/match/13750">
<span class="teamName">NEW</span>
<span class="badge-20 t7609"></span>
<span class="score">1 <span>-</span>4</span>
<span class="badge-20 t8951"></span>
<span class="teamName">BHA</span>
<span class="icn arrow-right"></span>
</a>
</div>
<div class="btnContainer">
<a class="btn-highlight" href="/clubs/131/Brighton-and-Hove-Albion/overview" role="btn">Visit <span class="visuallyHidden">Brighton and Hove Albion </span>Club Page<span class="icn arrow-right-w"></span></a>
</div>
</div>
<div class="teamPerformanceStandingsArea" style="display:none;">
<header>
<h3 class="subHeader left">Performance Chart</h3>
<a class="btn right" href="/stats/comparison">Compare against another team<span class="icn arrow-right"></span></a>
</header>
<div class="teamPerformanceStandingsContainer"></div>
</div>
</td>
</tr>
<tr class="" data-compseason="39" data-filtered-entry-size="12" data-filtered-table-row="360" data-filtered-table-row-abbr="360" data-filtered-table-row-name="Wolves" data-filtered-table-row-opta="t7136">
<td class="pos" tabindex="0">
<span class="value">12</span>
</td>
<td class="team" scope="row">
<a href="/clubs/38/Wolverhampton-Wanderers/overview"><span alt="" class="badge-25 t7136"></span><span class="long">Wolverhampton Wanderers</span><span class="short">WOL</span></a>
</td>
<td>22</td>
<td>2</td>
<td>7</td>
<td>13</td>
<td class="hideSmall">20</td>
<td class="hideSmall">35</td>
<td> 
        -15

 </td>
<td class="points">13</td>
<td class="form hideMed">
<ul>
<li class="draw button-tooltip" id="Tooltip" role="tooltip" tabindex="0">D
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13693" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 29 February 2016</span>
<span class="teamName">ARS</span>
<span class="badge-20 t7594"></span>
<span class="score">1 <span>-</span>1</span>
<span class="badge-20 t7136"></span>
<span class="teamName">WOL</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="draw button-tooltip" id="Tooltip" role="tooltip" tabindex="0">D
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13708" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Tuesday 8 March 2016</span>
<span class="teamName">WBA</span>
<span class="badge-20 t7595"></span>
<span class="score">0 <span>-</span>0</span>
<span class="badge-20 t7136"></span>
<span class="teamName">WOL</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="draw button-tooltip" id="Tooltip" role="tooltip" tabindex="0">D
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13720" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 14 March 2016</span>
<span class="teamName">WOL</span>
<span class="badge-20 t7136"></span>
<span class="score">1 <span>-</span>1</span>
<span class="badge-20 t8950"></span>
<span class="teamName">SWA</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13726" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 21 March 2016</span>
<span class="teamName">BLB</span>
<span class="badge-20 t7590"></span>
<span class="score">2 <span>-</span>1</span>
<span class="badge-20 t7136"></span>
<span class="teamName">WOL</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13753" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Wednesday 13 April 2016</span>
<span class="teamName">WOL</span>
<span class="badge-20 t7136"></span>
<span class="score">0 <span>-</span>3</span>
<span class="badge-20 t6912"></span>
<span class="teamName">FUL</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
</ul>
<td class="nextMatchCol hideMed">
</td>
</td>
</tr>
<tr class="expandable" data-filtered-table-row-expander="360">
<td colspan="13">
<a class="expandableTeam" href="/clubs/38/Wolverhampton-Wanderers/overview">
<span class="badge-50 t7136"></span>
<span class="teamName">Wolverhampton Wanderers</span>
</a>
<div class="expandableFixtures">
<div class="resultWidget">
<div class="label"><strong>Recent Result</strong> - Monday 29 February 2016</div>
<a class="matchAbridged pre" href="/match/13753">
<span class="teamName">WOL</span>
<span class="badge-20 t7136"></span>
<span class="score">0 <span>-</span>3</span>
<span class="badge-20 t6912"></span>
<span class="teamName">FUL</span>
<span class="icn arrow-right"></span>
</a>
</div>
<div class="btnContainer">
<a class="btn-highlight" href="/clubs/38/Wolverhampton-Wanderers/overview" role="btn">Visit <span class="visuallyHidden">Wolverhampton Wanderers </span>Club Page<span class="icn arrow-right-w"></span></a>
</div>
</div>
<div class="teamPerformanceStandingsArea" style="display:none;">
<header>
<h3 class="subHeader left">Performance Chart</h3>
<a class="btn right" href="/stats/comparison">Compare against another team<span class="icn arrow-right"></span></a>
</header>
<div class="teamPerformanceStandingsContainer"></div>
</div>
</td>
</tr>
</tbody>
</table>
</div>, <div class="table wrapper col-12">
<table>
<summary class="visuallyHidden">This table charts the Premier League teams</summary>
<thead>
<tr>
<th class="text-centre" scope="col">
<div class="thFull">Position</div>
<div class="thShort">Pos</div>
</th>
<th class="team" scope="col">Club</th>
<th scope="col">
<div class="thFull">Played</div>
<div class="thShort">Pl</div>
</th>
<th scope="col">
<div class="thFull">Won</div>
<div class="thShort">W</div>
</th>
<th scope="col">
<div class="thFull">Drawn</div>
<div class="thShort">D</div>
</th>
<th scope="col">
<div class="thFull">Lost</div>
<div class="thShort">L</div>
</th>
<th class="hideSmall" scope="col"><abbr title="Goals For">GF</abbr></th>
<th class="hideSmall" scope="col"><abbr title="Goals Against">GA</abbr></th>
<th scope="col"><abbr title="Goal Difference">GD</abbr></th>
<th class="points" scope="col">
<div class="thFull">Points</div>
<div class="thShort">Pts</div>
</th>
<th class="teamForm hideMed" scope="col">Form</th>
<th class="hideMed text-centre" scope="col">Next</th>
</tr>
</thead>
<tbody class="tableBodyContainer">
<tr class="tableDark" data-compseason="35" data-filtered-entry-size="8" data-filtered-table-row="317" data-filtered-table-row-abbr="317" data-filtered-table-row-name="Manchester City" data-filtered-table-row-opta="t6718">
<td class="pos button-tooltip" id="Tooltip" role="tooltip" tabindex="0">
<span class="value">1</span>
<span class="movement none">
<span class="tooltipContainer tooltip-left" role="tooltip">
<span class="tooltip-content">Previous Position
                            <span class="resultHighlight">
                                1
                            </span>
</span>
</span>
</span>
</td>
<td class="team" scope="row">
<a href="/clubs/11/Manchester-City/overview"><span alt="" class="badge-25 t6718"></span><span class="long">Manchester City</span><span class="short">MCI</span></a>
</td>
<td>7</td>
<td>6</td>
<td>1</td>
<td>0</td>
<td class="hideSmall">21</td>
<td class="hideSmall">7</td>
<td> 
        +14

 </td>
<td class="points">19</td>
<td class="form hideMed">
<ul>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12078" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 9 April 2016</span>
<span class="teamName">MCI</span>
<span class="badge-20 t6718"></span>
<span class="score">3 <span>-</span>0</span>
<span class="badge-20 t7632"></span>
<span class="teamName">WHU</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12086" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 16 April 2016</span>
<span class="teamName">LIV</span>
<span class="badge-20 t6717"></span>
<span class="score">0 <span>-</span>2</span>
<span class="badge-20 t6718"></span>
<span class="teamName">MCI</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12105" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 30 April 2016</span>
<span class="teamName">MCI</span>
<span class="badge-20 t6718"></span>
<span class="score">2 <span>-</span>0</span>
<span class="badge-20 t6748"></span>
<span class="teamName">BLB</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="draw button-tooltip" id="Tooltip" role="tooltip" tabindex="0">D
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12111" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Tuesday 3 May 2016</span>
<span class="teamName">EVE</span>
<span class="badge-20 t6749"></span>
<span class="score">4 <span>-</span>4</span>
<span class="badge-20 t6718"></span>
<span class="teamName">MCI</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12113" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 7 May 2016</span>
<span class="teamName">MCI</span>
<span class="badge-20 t6718"></span>
<span class="score">5 <span>-</span>0</span>
<span class="badge-20 t6886"></span>
<span class="teamName">FUL</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
</ul>
<td class="nextMatchCol hideMed">
</td>
</td>
</tr>
<tr class="expandable" data-filtered-table-row-expander="317">
<td colspan="13">
<a class="expandableTeam" href="/clubs/11/Manchester-City/overview">
<span class="badge-50 t6718"></span>
<span class="teamName">Manchester City</span>
</a>
<div class="expandableFixtures">
<div class="resultWidget">
<div class="label"><strong>Recent Result</strong> - Saturday 9 April 2016</div>
<a class="matchAbridged pre" href="/match/12113">
<span class="teamName">MCI</span>
<span class="badge-20 t6718"></span>
<span class="score">5 <span>-</span>0</span>
<span class="badge-20 t6886"></span>
<span class="teamName">FUL</span>
<span class="icn arrow-right"></span>
</a>
</div>
<div class="btnContainer">
<a class="btn-highlight" href="/clubs/11/Manchester-City/overview" role="btn">Visit <span class="visuallyHidden">Manchester City </span>Club Page<span class="icn arrow-right-w"></span></a>
</div>
</div>
<div class="teamPerformanceStandingsArea" style="display:none;">
<header>
<h3 class="subHeader left">Performance Chart</h3>
<a class="btn right" href="/stats/comparison">Compare against another team<span class="icn arrow-right"></span></a>
</header>
<div class="teamPerformanceStandingsContainer"></div>
</div>
</td>
</tr>
<tr class="" data-compseason="35" data-filtered-entry-size="8" data-filtered-table-row="313" data-filtered-table-row-abbr="313" data-filtered-table-row-name="Everton" data-filtered-table-row-opta="t6749">
<td class="pos button-tooltip" id="Tooltip" role="tooltip" tabindex="0">
<span class="value">2</span>
<span class="movement none">
<span class="tooltipContainer tooltip-left" role="tooltip">
<span class="tooltip-content">Previous Position
                            <span class="resultHighlight">
                                2
                            </span>
</span>
</span>
</span>
</td>
<td class="team" scope="row">
<a href="/clubs/7/Everton/overview"><span alt="" class="badge-25 t6749"></span><span class="long">Everton</span><span class="short">EVE</span></a>
</td>
<td>7</td>
<td>4</td>
<td>1</td>
<td>2</td>
<td class="hideSmall">14</td>
<td class="hideSmall">15</td>
<td> 
        -1

 </td>
<td class="points">13</td>
<td class="form hideMed">
<ul>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12069" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 2 April 2016</span>
<span class="teamName">EVE</span>
<span class="badge-20 t6749"></span>
<span class="score">2 <span>-</span>1</span>
<span class="badge-20 t6748"></span>
<span class="teamName">BLB</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12076" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 9 April 2016</span>
<span class="teamName">EVE</span>
<span class="badge-20 t6749"></span>
<span class="score">0 <span>-</span>4</span>
<span class="badge-20 t6717"></span>
<span class="teamName">LIV</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12085" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 16 April 2016</span>
<span class="teamName">FUL</span>
<span class="badge-20 t6886"></span>
<span class="score">2 <span>-</span>3</span>
<span class="badge-20 t6749"></span>
<span class="teamName">EVE</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12104" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 30 April 2016</span>
<span class="teamName">EVE</span>
<span class="badge-20 t6749"></span>
<span class="score">4 <span>-</span>3</span>
<span class="badge-20 t7632"></span>
<span class="teamName">WHU</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="draw button-tooltip" id="Tooltip" role="tooltip" tabindex="0">D
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12111" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Tuesday 3 May 2016</span>
<span class="teamName">EVE</span>
<span class="badge-20 t6749"></span>
<span class="score">4 <span>-</span>4</span>
<span class="badge-20 t6718"></span>
<span class="teamName">MCI</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
</ul>
<td class="nextMatchCol hideMed">
</td>
</td>
</tr>
<tr class="expandable" data-filtered-table-row-expander="313">
<td colspan="13">
<a class="expandableTeam" href="/clubs/7/Everton/overview">
<span class="badge-50 t6749"></span>
<span class="teamName">Everton</span>
</a>
<div class="expandableFixtures">
<div class="resultWidget">
<div class="label"><strong>Recent Result</strong> - Saturday 2 April 2016</div>
<a class="matchAbridged pre" href="/match/12111">
<span class="teamName">EVE</span>
<span class="badge-20 t6749"></span>
<span class="score">4 <span>-</span>4</span>
<span class="badge-20 t6718"></span>
<span class="teamName">MCI</span>
<span class="icn arrow-right"></span>
</a>
</div>
<div class="btnContainer">
<a class="btn-highlight" href="/clubs/7/Everton/overview" role="btn">Visit <span class="visuallyHidden">Everton </span>Club Page<span class="icn arrow-right-w"></span></a>
</div>
</div>
<div class="teamPerformanceStandingsArea" style="display:none;">
<header>
<h3 class="subHeader left">Performance Chart</h3>
<a class="btn right" href="/stats/comparison">Compare against another team<span class="icn arrow-right"></span></a>
</header>
<div class="teamPerformanceStandingsContainer"></div>
</div>
</td>
</tr>
<tr class="" data-compseason="35" data-filtered-entry-size="8" data-filtered-table-row="311" data-filtered-table-row-abbr="311" data-filtered-table-row-name="Chelsea" data-filtered-table-row-opta="t7141">
<td class="pos button-tooltip" id="Tooltip" role="tooltip" tabindex="0">
<span class="value">3</span>
<span class="movement none">
<span class="tooltipContainer tooltip-left" role="tooltip">
<span class="tooltip-content">Previous Position
                            <span class="resultHighlight">
                                3
                            </span>
</span>
</span>
</span>
</td>
<td class="team" scope="row">
<a href="/clubs/4/Chelsea/overview"><span alt="" class="badge-25 t7141"></span><span class="long">Chelsea</span><span class="short">CHE</span></a>
</td>
<td>7</td>
<td>3</td>
<td>2</td>
<td>2</td>
<td class="hideSmall">16</td>
<td class="hideSmall">13</td>
<td> 
        +3

 </td>
<td class="points">11</td>
<td class="form hideMed">
<ul>
<li class="draw button-tooltip" id="Tooltip" role="tooltip" tabindex="0">D
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12062" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 19 March 2016</span>
<span class="teamName">CHE</span>
<span class="badge-20 t7141"></span>
<span class="score">2 <span>-</span>2</span>
<span class="badge-20 t7632"></span>
<span class="teamName">WHU</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12068" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 2 April 2016</span>
<span class="teamName">CHE</span>
<span class="badge-20 t7141"></span>
<span class="score">6 <span>-</span>2</span>
<span class="badge-20 t7587"></span>
<span class="teamName">RDG</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12077" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 9 April 2016</span>
<span class="teamName">FUL</span>
<span class="badge-20 t6886"></span>
<span class="score">0 <span>-</span>2</span>
<span class="badge-20 t7141"></span>
<span class="teamName">CHE</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="draw button-tooltip" id="Tooltip" role="tooltip" tabindex="0">D
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12099" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Friday 29 April 2016</span>
<span class="teamName">CHE</span>
<span class="badge-20 t7141"></span>
<span class="score">2 <span>-</span>2</span>
<span class="badge-20 t6717"></span>
<span class="teamName">LIV</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12112" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 7 May 2016</span>
<span class="teamName">BLB</span>
<span class="badge-20 t6748"></span>
<span class="score">3 <span>-</span>0</span>
<span class="badge-20 t7141"></span>
<span class="teamName">CHE</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
</ul>
<td class="nextMatchCol hideMed">
</td>
</td>
</tr>
<tr class="expandable" data-filtered-table-row-expander="311">
<td colspan="13">
<a class="expandableTeam" href="/clubs/4/Chelsea/overview">
<span class="badge-50 t7141"></span>
<span class="teamName">Chelsea</span>
</a>
<div class="expandableFixtures">
<div class="resultWidget">
<div class="label"><strong>Recent Result</strong> - Saturday 19 March 2016</div>
<a class="matchAbridged pre" href="/match/12112">
<span class="teamName">BLB</span>
<span class="badge-20 t6748"></span>
<span class="score">3 <span>-</span>0</span>
<span class="badge-20 t7141"></span>
<span class="teamName">CHE</span>
<span class="icn arrow-right"></span>
</a>
</div>
<div class="btnContainer">
<a class="btn-highlight" href="/clubs/4/Chelsea/overview" role="btn">Visit <span class="visuallyHidden">Chelsea </span>Club Page<span class="icn arrow-right-w"></span></a>
</div>
</div>
<div class="teamPerformanceStandingsArea" style="display:none;">
<header>
<h3 class="subHeader left">Performance Chart</h3>
<a class="btn right" href="/stats/comparison">Compare against another team<span class="icn arrow-right"></span></a>
</header>
<div class="teamPerformanceStandingsContainer"></div>
</div>
</td>
</tr>
<tr class="" data-compseason="35" data-filtered-entry-size="8" data-filtered-table-row="316" data-filtered-table-row-abbr="316" data-filtered-table-row-name="Liverpool" data-filtered-table-row-opta="t6717">
<td class="pos button-tooltip" id="Tooltip" role="tooltip" tabindex="0">
<span class="value">4</span>
<span class="movement none">
<span class="tooltipContainer tooltip-left" role="tooltip">
<span class="tooltip-content">Previous Position
                            <span class="resultHighlight">
                                4
                            </span>
</span>
</span>
</span>
</td>
<td class="team" scope="row">
<a href="/clubs/10/Liverpool/overview"><span alt="" class="badge-25 t6717"></span><span class="long">Liverpool</span><span class="short">LIV</span></a>
</td>
<td>7</td>
<td>2</td>
<td>2</td>
<td>3</td>
<td class="hideSmall">13</td>
<td class="hideSmall">11</td>
<td> 
        +2

 </td>
<td class="points">8</td>
<td class="form hideMed">
<ul>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12070" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 2 April 2016</span>
<span class="teamName">FUL</span>
<span class="badge-20 t6886"></span>
<span class="score">1 <span>-</span>5</span>
<span class="badge-20 t6717"></span>
<span class="teamName">LIV</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12076" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 9 April 2016</span>
<span class="teamName">EVE</span>
<span class="badge-20 t6749"></span>
<span class="score">0 <span>-</span>4</span>
<span class="badge-20 t6717"></span>
<span class="teamName">LIV</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12086" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 16 April 2016</span>
<span class="teamName">LIV</span>
<span class="badge-20 t6717"></span>
<span class="score">0 <span>-</span>2</span>
<span class="badge-20 t6718"></span>
<span class="teamName">MCI</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="draw button-tooltip" id="Tooltip" role="tooltip" tabindex="0">D
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12097" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 23 April 2016</span>
<span class="teamName">WHU</span>
<span class="badge-20 t7632"></span>
<span class="score">0 <span>-</span>0</span>
<span class="badge-20 t6717"></span>
<span class="teamName">LIV</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="draw button-tooltip" id="Tooltip" role="tooltip" tabindex="0">D
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12099" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Friday 29 April 2016</span>
<span class="teamName">CHE</span>
<span class="badge-20 t7141"></span>
<span class="score">2 <span>-</span>2</span>
<span class="badge-20 t6717"></span>
<span class="teamName">LIV</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
</ul>
<td class="nextMatchCol hideMed">
</td>
</td>
</tr>
<tr class="expandable" data-filtered-table-row-expander="316">
<td colspan="13">
<a class="expandableTeam" href="/clubs/10/Liverpool/overview">
<span class="badge-50 t6717"></span>
<span class="teamName">Liverpool</span>
</a>
<div class="expandableFixtures">
<div class="resultWidget">
<div class="label"><strong>Recent Result</strong> - Saturday 2 April 2016</div>
<a class="matchAbridged pre" href="/match/12099">
<span class="teamName">CHE</span>
<span class="badge-20 t7141"></span>
<span class="score">2 <span>-</span>2</span>
<span class="badge-20 t6717"></span>
<span class="teamName">LIV</span>
<span class="icn arrow-right"></span>
</a>
</div>
<div class="btnContainer">
<a class="btn-highlight" href="/clubs/10/Liverpool/overview" role="btn">Visit <span class="visuallyHidden">Liverpool </span>Club Page<span class="icn arrow-right-w"></span></a>
</div>
</div>
<div class="teamPerformanceStandingsArea" style="display:none;">
<header>
<h3 class="subHeader left">Performance Chart</h3>
<a class="btn right" href="/stats/comparison">Compare against another team<span class="icn arrow-right"></span></a>
</header>
<div class="teamPerformanceStandingsContainer"></div>
</div>
</td>
</tr>
<tr class="" data-compseason="35" data-filtered-entry-size="8" data-filtered-table-row="309" data-filtered-table-row-abbr="309" data-filtered-table-row-name="Blackburn" data-filtered-table-row-opta="t6748">
<td class="pos button-tooltip" id="Tooltip" role="tooltip" tabindex="0">
<span class="value">5</span>
<span class="movement up">
<span class="tooltipContainer tooltip-left" role="tooltip">
<span class="tooltip-content">Previous Position
                            <span class="resultHighlight">
                                6
                            </span>
</span>
</span>
</span>
</td>
<td class="team" scope="row">
<a href="/clubs/3/Blackburn-Rovers/overview"><span alt="" class="badge-25 t6748"></span><span class="long">Blackburn Rovers</span><span class="short">BLB</span></a>
</td>
<td>7</td>
<td>2</td>
<td>2</td>
<td>3</td>
<td class="hideSmall">9</td>
<td class="hideSmall">9</td>
<td> 
        0

 </td>
<td class="points">8</td>
<td class="form hideMed">
<ul>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12069" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 2 April 2016</span>
<span class="teamName">EVE</span>
<span class="badge-20 t6749"></span>
<span class="score">2 <span>-</span>1</span>
<span class="badge-20 t6748"></span>
<span class="teamName">BLB</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="draw button-tooltip" id="Tooltip" role="tooltip" tabindex="0">D
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12095" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 23 April 2016</span>
<span class="teamName">RDG</span>
<span class="badge-20 t7587"></span>
<span class="score">1 <span>-</span>1</span>
<span class="badge-20 t6748"></span>
<span class="teamName">BLB</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="draw button-tooltip" id="Tooltip" role="tooltip" tabindex="0">D
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12098" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Wednesday 27 April 2016</span>
<span class="teamName">BLB</span>
<span class="badge-20 t6748"></span>
<span class="score">1 <span>-</span>1</span>
<span class="badge-20 t7632"></span>
<span class="teamName">WHU</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12105" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 30 April 2016</span>
<span class="teamName">MCI</span>
<span class="badge-20 t6718"></span>
<span class="score">2 <span>-</span>0</span>
<span class="badge-20 t6748"></span>
<span class="teamName">BLB</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12112" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 7 May 2016</span>
<span class="teamName">BLB</span>
<span class="badge-20 t6748"></span>
<span class="score">3 <span>-</span>0</span>
<span class="badge-20 t7141"></span>
<span class="teamName">CHE</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
</ul>
<td class="nextMatchCol hideMed">
</td>
</td>
</tr>
<tr class="expandable" data-filtered-table-row-expander="309">
<td colspan="13">
<a class="expandableTeam" href="/clubs/3/Blackburn-Rovers/overview">
<span class="badge-50 t6748"></span>
<span class="teamName">Blackburn Rovers</span>
</a>
<div class="expandableFixtures">
<div class="resultWidget">
<div class="label"><strong>Recent Result</strong> - Saturday 2 April 2016</div>
<a class="matchAbridged pre" href="/match/12112">
<span class="teamName">BLB</span>
<span class="badge-20 t6748"></span>
<span class="score">3 <span>-</span>0</span>
<span class="badge-20 t7141"></span>
<span class="teamName">CHE</span>
<span class="icn arrow-right"></span>
</a>
</div>
<div class="btnContainer">
<a class="btn-highlight" href="/clubs/3/Blackburn-Rovers/overview" role="btn">Visit <span class="visuallyHidden">Blackburn Rovers </span>Club Page<span class="icn arrow-right-w"></span></a>
</div>
</div>
<div class="teamPerformanceStandingsArea" style="display:none;">
<header>
<h3 class="subHeader left">Performance Chart</h3>
<a class="btn right" href="/stats/comparison">Compare against another team<span class="icn arrow-right"></span></a>
</header>
<div class="teamPerformanceStandingsContainer"></div>
</div>
</td>
</tr>
<tr class="" data-compseason="35" data-filtered-entry-size="8" data-filtered-table-row="314" data-filtered-table-row-abbr="314" data-filtered-table-row-name="Fulham" data-filtered-table-row-opta="t6886">
<td class="pos button-tooltip" id="Tooltip" role="tooltip" tabindex="0">
<span class="value">6</span>
<span class="movement down">
<span class="tooltipContainer tooltip-left" role="tooltip">
<span class="tooltip-content">Previous Position
                            <span class="resultHighlight">
                                5
                            </span>
</span>
</span>
</span>
</td>
<td class="team" scope="row">
<a href="/clubs/34/Fulham/overview"><span alt="" class="badge-25 t6886"></span><span class="long">Fulham</span><span class="short">FUL</span></a>
</td>
<td>7</td>
<td>2</td>
<td>1</td>
<td>4</td>
<td class="hideSmall">9</td>
<td class="hideSmall">19</td>
<td> 
        -10

 </td>
<td class="points">7</td>
<td class="form hideMed">
<ul>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12070" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 2 April 2016</span>
<span class="teamName">FUL</span>
<span class="badge-20 t6886"></span>
<span class="score">1 <span>-</span>5</span>
<span class="badge-20 t6717"></span>
<span class="teamName">LIV</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12077" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 9 April 2016</span>
<span class="teamName">FUL</span>
<span class="badge-20 t6886"></span>
<span class="score">0 <span>-</span>2</span>
<span class="badge-20 t7141"></span>
<span class="teamName">CHE</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12085" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 16 April 2016</span>
<span class="teamName">FUL</span>
<span class="badge-20 t6886"></span>
<span class="score">2 <span>-</span>3</span>
<span class="badge-20 t6749"></span>
<span class="teamName">EVE</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12108" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 30 April 2016</span>
<span class="teamName">RDG</span>
<span class="badge-20 t7587"></span>
<span class="score">1 <span>-</span>2</span>
<span class="badge-20 t6886"></span>
<span class="teamName">FUL</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12113" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 7 May 2016</span>
<span class="teamName">MCI</span>
<span class="badge-20 t6718"></span>
<span class="score">5 <span>-</span>0</span>
<span class="badge-20 t6886"></span>
<span class="teamName">FUL</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
</ul>
<td class="nextMatchCol hideMed">
</td>
</td>
</tr>
<tr class="expandable" data-filtered-table-row-expander="314">
<td colspan="13">
<a class="expandableTeam" href="/clubs/34/Fulham/overview">
<span class="badge-50 t6886"></span>
<span class="teamName">Fulham</span>
</a>
<div class="expandableFixtures">
<div class="resultWidget">
<div class="label"><strong>Recent Result</strong> - Saturday 2 April 2016</div>
<a class="matchAbridged pre" href="/match/12113">
<span class="teamName">MCI</span>
<span class="badge-20 t6718"></span>
<span class="score">5 <span>-</span>0</span>
<span class="badge-20 t6886"></span>
<span class="teamName">FUL</span>
<span class="icn arrow-right"></span>
</a>
</div>
<div class="btnContainer">
<a class="btn-highlight" href="/clubs/34/Fulham/overview" role="btn">Visit <span class="visuallyHidden">Fulham </span>Club Page<span class="icn arrow-right-w"></span></a>
</div>
</div>
<div class="teamPerformanceStandingsArea" style="display:none;">
<header>
<h3 class="subHeader left">Performance Chart</h3>
<a class="btn right" href="/stats/comparison">Compare against another team<span class="icn arrow-right"></span></a>
</header>
<div class="teamPerformanceStandingsContainer"></div>
</div>
</td>
</tr>
<tr class="" data-compseason="35" data-filtered-entry-size="8" data-filtered-table-row="322" data-filtered-table-row-abbr="322" data-filtered-table-row-name="Reading" data-filtered-table-row-opta="t7587">
<td class="pos button-tooltip" id="Tooltip" role="tooltip" tabindex="0">
<span class="value">7</span>
<span class="movement none">
<span class="tooltipContainer tooltip-left" role="tooltip">
<span class="tooltip-content">Previous Position
                            <span class="resultHighlight">
                                7
                            </span>
</span>
</span>
</span>
</td>
<td class="team" scope="row">
<a href="/clubs/40/Reading/overview"><span alt="" class="badge-25 t7587"></span><span class="long">Reading</span><span class="short">RDG</span></a>
</td>
<td>7</td>
<td>1</td>
<td>2</td>
<td>4</td>
<td class="hideSmall">9</td>
<td class="hideSmall">13</td>
<td> 
        -4

 </td>
<td class="points">5</td>
<td class="form hideMed">
<ul>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12065" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 19 March 2016</span>
<span class="teamName">LIV</span>
<span class="badge-20 t6717"></span>
<span class="score">1 <span>-</span>4</span>
<span class="badge-20 t7587"></span>
<span class="teamName">RDG</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12068" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 2 April 2016</span>
<span class="teamName">CHE</span>
<span class="badge-20 t7141"></span>
<span class="score">6 <span>-</span>2</span>
<span class="badge-20 t7587"></span>
<span class="teamName">RDG</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="draw button-tooltip" id="Tooltip" role="tooltip" tabindex="0">D
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12090" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 16 April 2016</span>
<span class="teamName">WHU</span>
<span class="badge-20 t7632"></span>
<span class="score">1 <span>-</span>1</span>
<span class="badge-20 t7587"></span>
<span class="teamName">RDG</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="draw button-tooltip" id="Tooltip" role="tooltip" tabindex="0">D
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12095" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 23 April 2016</span>
<span class="teamName">RDG</span>
<span class="badge-20 t7587"></span>
<span class="score">1 <span>-</span>1</span>
<span class="badge-20 t6748"></span>
<span class="teamName">BLB</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12108" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 30 April 2016</span>
<span class="teamName">RDG</span>
<span class="badge-20 t7587"></span>
<span class="score">1 <span>-</span>2</span>
<span class="badge-20 t6886"></span>
<span class="teamName">FUL</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
</ul>
<td class="nextMatchCol hideMed">
</td>
</td>
</tr>
<tr class="expandable" data-filtered-table-row-expander="322">
<td colspan="13">
<a class="expandableTeam" href="/clubs/40/Reading/overview">
<span class="badge-50 t7587"></span>
<span class="teamName">Reading</span>
</a>
<div class="expandableFixtures">
<div class="resultWidget">
<div class="label"><strong>Recent Result</strong> - Saturday 19 March 2016</div>
<a class="matchAbridged pre" href="/match/12108">
<span class="teamName">RDG</span>
<span class="badge-20 t7587"></span>
<span class="score">1 <span>-</span>2</span>
<span class="badge-20 t6886"></span>
<span class="teamName">FUL</span>
<span class="icn arrow-right"></span>
</a>
</div>
<div class="btnContainer">
<a class="btn-highlight" href="/clubs/40/Reading/overview" role="btn">Visit <span class="visuallyHidden">Reading </span>Club Page<span class="icn arrow-right-w"></span></a>
</div>
</div>
<div class="teamPerformanceStandingsArea" style="display:none;">
<header>
<h3 class="subHeader left">Performance Chart</h3>
<a class="btn right" href="/stats/comparison">Compare against another team<span class="icn arrow-right"></span></a>
</header>
<div class="teamPerformanceStandingsContainer"></div>
</div>
</td>
</tr>
<tr class="" data-compseason="35" data-filtered-entry-size="8" data-filtered-table-row="329" data-filtered-table-row-abbr="329" data-filtered-table-row-name="West Ham United" data-filtered-table-row-opta="t7632">
<td class="pos button-tooltip" id="Tooltip" role="tooltip" tabindex="0">
<span class="value">8</span>
<span class="movement none">
<span class="tooltipContainer tooltip-left" role="tooltip">
<span class="tooltip-content">Previous Position
                            <span class="resultHighlight">
                                8
                            </span>
</span>
</span>
</span>
</td>
<td class="team" scope="row">
<a href="/clubs/25/West-Ham-United/overview"><span alt="" class="badge-25 t7632"></span><span class="long">West Ham United</span><span class="short">WHU</span></a>
</td>
<td>7</td>
<td>0</td>
<td>5</td>
<td>2</td>
<td class="hideSmall">9</td>
<td class="hideSmall">13</td>
<td> 
        -4

 </td>
<td class="points">5</td>
<td class="form hideMed">
<ul>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12078" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 9 April 2016</span>
<span class="teamName">MCI</span>
<span class="badge-20 t6718"></span>
<span class="score">3 <span>-</span>0</span>
<span class="badge-20 t7632"></span>
<span class="teamName">WHU</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="draw button-tooltip" id="Tooltip" role="tooltip" tabindex="0">D
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12090" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 16 April 2016</span>
<span class="teamName">WHU</span>
<span class="badge-20 t7632"></span>
<span class="score">1 <span>-</span>1</span>
<span class="badge-20 t7587"></span>
<span class="teamName">RDG</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="draw button-tooltip" id="Tooltip" role="tooltip" tabindex="0">D
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12097" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 23 April 2016</span>
<span class="teamName">WHU</span>
<span class="badge-20 t7632"></span>
<span class="score">0 <span>-</span>0</span>
<span class="badge-20 t6717"></span>
<span class="teamName">LIV</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="draw button-tooltip" id="Tooltip" role="tooltip" tabindex="0">D
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12098" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Wednesday 27 April 2016</span>
<span class="teamName">BLB</span>
<span class="badge-20 t6748"></span>
<span class="score">1 <span>-</span>1</span>
<span class="badge-20 t7632"></span>
<span class="teamName">WHU</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12104" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 30 April 2016</span>
<span class="teamName">EVE</span>
<span class="badge-20 t6749"></span>
<span class="score">4 <span>-</span>3</span>
<span class="badge-20 t7632"></span>
<span class="teamName">WHU</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
</ul>
<td class="nextMatchCol hideMed">
</td>
</td>
</tr>
<tr class="expandable" data-filtered-table-row-expander="329">
<td colspan="13">
<a class="expandableTeam" href="/clubs/25/West-Ham-United/overview">
<span class="badge-50 t7632"></span>
<span class="teamName">West Ham United</span>
</a>
<div class="expandableFixtures">
<div class="resultWidget">
<div class="label"><strong>Recent Result</strong> - Saturday 9 April 2016</div>
<a class="matchAbridged pre" href="/match/12104">
<span class="teamName">EVE</span>
<span class="badge-20 t6749"></span>
<span class="score">4 <span>-</span>3</span>
<span class="badge-20 t7632"></span>
<span class="teamName">WHU</span>
<span class="icn arrow-right"></span>
</a>
</div>
<div class="btnContainer">
<a class="btn-highlight" href="/clubs/25/West-Ham-United/overview" role="btn">Visit <span class="visuallyHidden">West Ham United </span>Club Page<span class="icn arrow-right-w"></span></a>
</div>
</div>
<div class="teamPerformanceStandingsArea" style="display:none;">
<header>
<h3 class="subHeader left">Performance Chart</h3>
<a class="btn right" href="/stats/comparison">Compare against another team<span class="icn arrow-right"></span></a>
</header>
<div class="teamPerformanceStandingsContainer"></div>
</div>
</td>
</tr>
</tbody>
</table>
</div>, <div class="table wrapper col-12">
<table>
<summary class="visuallyHidden">This table charts the Premier League teams</summary>
<thead>
<tr>
<th class="text-centre" scope="col">
<div class="thFull">Position</div>
<div class="thShort">Pos</div>
</th>
<th class="team" scope="col">Club</th>
<th scope="col">
<div class="thFull">Played</div>
<div class="thShort">Pl</div>
</th>
<th scope="col">
<div class="thFull">Won</div>
<div class="thShort">W</div>
</th>
<th scope="col">
<div class="thFull">Drawn</div>
<div class="thShort">D</div>
</th>
<th scope="col">
<div class="thFull">Lost</div>
<div class="thShort">L</div>
</th>
<th class="hideSmall" scope="col"><abbr title="Goals For">GF</abbr></th>
<th class="hideSmall" scope="col"><abbr title="Goals Against">GA</abbr></th>
<th scope="col"><abbr title="Goal Difference">GD</abbr></th>
<th class="points" scope="col">
<div class="thFull">Points</div>
<div class="thShort">Pts</div>
</th>
<th class="teamForm hideMed" scope="col">Form</th>
<th class="hideMed text-centre" scope="col">Next</th>
</tr>
</thead>
<tbody class="tableBodyContainer">
<tr class="tableDark" data-compseason="35" data-filtered-entry-size="8" data-filtered-table-row="319" data-filtered-table-row-abbr="319" data-filtered-table-row-name="Middlesbrough" data-filtered-table-row-opta="t7143">
<td class="pos" tabindex="0">
<span class="value">1</span>
</td>
<td class="team" scope="row">
<a href="/clubs/13/Middlesbrough/overview"><span alt="" class="badge-25 t7143"></span><span class="long">Middlesbrough</span><span class="short">MID</span></a>
</td>
<td>7</td>
<td>6</td>
<td>1</td>
<td>0</td>
<td class="hideSmall">14</td>
<td class="hideSmall">6</td>
<td> 
        +8

 </td>
<td class="points">19</td>
<td class="form hideMed">
<ul>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12050" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Tuesday 8 March 2016</span>
<span class="teamName">ARS</span>
<span class="badge-20 t7606"></span>
<span class="score">1 <span>-</span>2</span>
<span class="badge-20 t7143"></span>
<span class="teamName">MID</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12054" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 12 March 2016</span>
<span class="teamName">MID</span>
<span class="badge-20 t7143"></span>
<span class="score">4 <span>-</span>1</span>
<span class="badge-20 t8879"></span>
<span class="teamName">LEI</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12080" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 9 April 2016</span>
<span class="teamName">MID</span>
<span class="badge-20 t7143"></span>
<span class="score">1 <span>-</span>0</span>
<span class="badge-20 t7631"></span>
<span class="teamName">TOT</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12091" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 16 April 2016</span>
<span class="teamName">WOL</span>
<span class="badge-20 t6746"></span>
<span class="score">2 <span>-</span>3</span>
<span class="badge-20 t7143"></span>
<span class="teamName">MID</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12107" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 30 April 2016</span>
<span class="teamName">MID</span>
<span class="badge-20 t7143"></span>
<span class="score">1 <span>-</span>0</span>
<span class="badge-20 t6753"></span>
<span class="teamName">WBA</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
</ul>
<td class="nextMatchCol hideMed">
</td>
</td>
</tr>
<tr class="expandable" data-filtered-table-row-expander="319">
<td colspan="13">
<a class="expandableTeam" href="/clubs/13/Middlesbrough/overview">
<span class="badge-50 t7143"></span>
<span class="teamName">Middlesbrough</span>
</a>
<div class="expandableFixtures">
<div class="resultWidget">
<div class="label"><strong>Recent Result</strong> - Tuesday 8 March 2016</div>
<a class="matchAbridged pre" href="/match/12107">
<span class="teamName">MID</span>
<span class="badge-20 t7143"></span>
<span class="score">1 <span>-</span>0</span>
<span class="badge-20 t6753"></span>
<span class="teamName">WBA</span>
<span class="icn arrow-right"></span>
</a>
</div>
<div class="btnContainer">
<a class="btn-highlight" href="/clubs/13/Middlesbrough/overview" role="btn">Visit <span class="visuallyHidden">Middlesbrough </span>Club Page<span class="icn arrow-right-w"></span></a>
</div>
</div>
<div class="teamPerformanceStandingsArea" style="display:none;">
<header>
<h3 class="subHeader left">Performance Chart</h3>
<a class="btn right" href="/stats/comparison">Compare against another team<span class="icn arrow-right"></span></a>
</header>
<div class="teamPerformanceStandingsContainer"></div>
</div>
</td>
</tr>
<tr class="" data-compseason="35" data-filtered-entry-size="8" data-filtered-table-row="325" data-filtered-table-row-abbr="325" data-filtered-table-row-name="Sunderland" data-filtered-table-row-opta="t6756">
<td class="pos" tabindex="0">
<span class="value">2</span>
</td>
<td class="team" scope="row">
<a href="/clubs/29/Sunderland/overview"><span alt="" class="badge-25 t6756"></span><span class="long">Sunderland</span><span class="short">SUN</span></a>
</td>
<td>7</td>
<td>4</td>
<td>1</td>
<td>2</td>
<td class="hideSmall">14</td>
<td class="hideSmall">8</td>
<td> 
        +6

 </td>
<td class="points">13</td>
<td class="form hideMed">
<ul>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12061" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 19 March 2016</span>
<span class="teamName">AVL</span>
<span class="badge-20 t7605"></span>
<span class="score">0 <span>-</span>1</span>
<span class="badge-20 t6756"></span>
<span class="teamName">SUN</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="draw button-tooltip" id="Tooltip" role="tooltip" tabindex="0">D
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12072" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Friday 8 April 2016</span>
<span class="teamName">SUN</span>
<span class="badge-20 t6756"></span>
<span class="score">1 <span>-</span>1</span>
<span class="badge-20 t8879"></span>
<span class="teamName">LEI</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12089" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 16 April 2016</span>
<span class="teamName">WBA</span>
<span class="badge-20 t6753"></span>
<span class="score">1 <span>-</span>4</span>
<span class="badge-20 t6756"></span>
<span class="teamName">SUN</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12096" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 23 April 2016</span>
<span class="teamName">SUN</span>
<span class="badge-20 t6756"></span>
<span class="score">1 <span>-</span>4</span>
<span class="badge-20 t7606"></span>
<span class="teamName">ARS</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12109" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 30 April 2016</span>
<span class="teamName">SUN</span>
<span class="badge-20 t6756"></span>
<span class="score">4 <span>-</span>1</span>
<span class="badge-20 t6746"></span>
<span class="teamName">WOL</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
</ul>
<td class="nextMatchCol hideMed">
</td>
</td>
</tr>
<tr class="expandable" data-filtered-table-row-expander="325">
<td colspan="13">
<a class="expandableTeam" href="/clubs/29/Sunderland/overview">
<span class="badge-50 t6756"></span>
<span class="teamName">Sunderland</span>
</a>
<div class="expandableFixtures">
<div class="resultWidget">
<div class="label"><strong>Recent Result</strong> - Saturday 19 March 2016</div>
<a class="matchAbridged pre" href="/match/12109">
<span class="teamName">SUN</span>
<span class="badge-20 t6756"></span>
<span class="score">4 <span>-</span>1</span>
<span class="badge-20 t6746"></span>
<span class="teamName">WOL</span>
<span class="icn arrow-right"></span>
</a>
</div>
<div class="btnContainer">
<a class="btn-highlight" href="/clubs/29/Sunderland/overview" role="btn">Visit <span class="visuallyHidden">Sunderland </span>Club Page<span class="icn arrow-right-w"></span></a>
</div>
</div>
<div class="teamPerformanceStandingsArea" style="display:none;">
<header>
<h3 class="subHeader left">Performance Chart</h3>
<a class="btn right" href="/stats/comparison">Compare against another team<span class="icn arrow-right"></span></a>
</header>
<div class="teamPerformanceStandingsContainer"></div>
</div>
</td>
</tr>
<tr class="" data-compseason="35" data-filtered-entry-size="8" data-filtered-table-row="315" data-filtered-table-row-abbr="315" data-filtered-table-row-name="Leicester City" data-filtered-table-row-opta="t8879">
<td class="pos" tabindex="0">
<span class="value">3</span>
</td>
<td class="team" scope="row">
<a href="/clubs/26/Leicester-City/overview"><span alt="" class="badge-25 t8879"></span><span class="long">Leicester City</span><span class="short">LEI</span></a>
</td>
<td>7</td>
<td>3</td>
<td>3</td>
<td>1</td>
<td class="hideSmall">16</td>
<td class="hideSmall">11</td>
<td> 
        +5

 </td>
<td class="points">12</td>
<td class="form hideMed">
<ul>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12054" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 12 March 2016</span>
<span class="teamName">MID</span>
<span class="badge-20 t7143"></span>
<span class="score">4 <span>-</span>1</span>
<span class="badge-20 t8879"></span>
<span class="teamName">LEI</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="draw button-tooltip" id="Tooltip" role="tooltip" tabindex="0">D
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12064" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 19 March 2016</span>
<span class="teamName">LEI</span>
<span class="badge-20 t8879"></span>
<span class="score">1 <span>-</span>1</span>
<span class="badge-20 t6753"></span>
<span class="teamName">WBA</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="draw button-tooltip" id="Tooltip" role="tooltip" tabindex="0">D
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12072" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Friday 8 April 2016</span>
<span class="teamName">SUN</span>
<span class="badge-20 t6756"></span>
<span class="score">1 <span>-</span>1</span>
<span class="badge-20 t8879"></span>
<span class="teamName">LEI</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12083" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 16 April 2016</span>
<span class="teamName">ARS</span>
<span class="badge-20 t7606"></span>
<span class="score">1 <span>-</span>2</span>
<span class="badge-20 t8879"></span>
<span class="teamName">LEI</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="draw button-tooltip" id="Tooltip" role="tooltip" tabindex="0">D
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12101" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 30 April 2016</span>
<span class="teamName">AVL</span>
<span class="badge-20 t7605"></span>
<span class="score">1 <span>-</span>1</span>
<span class="badge-20 t8879"></span>
<span class="teamName">LEI</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
</ul>
<td class="nextMatchCol hideMed">
</td>
</td>
</tr>
<tr class="expandable" data-filtered-table-row-expander="315">
<td colspan="13">
<a class="expandableTeam" href="/clubs/26/Leicester-City/overview">
<span class="badge-50 t8879"></span>
<span class="teamName">Leicester City</span>
</a>
<div class="expandableFixtures">
<div class="resultWidget">
<div class="label"><strong>Recent Result</strong> - Saturday 12 March 2016</div>
<a class="matchAbridged pre" href="/match/12101">
<span class="teamName">AVL</span>
<span class="badge-20 t7605"></span>
<span class="score">1 <span>-</span>1</span>
<span class="badge-20 t8879"></span>
<span class="teamName">LEI</span>
<span class="icn arrow-right"></span>
</a>
</div>
<div class="btnContainer">
<a class="btn-highlight" href="/clubs/26/Leicester-City/overview" role="btn">Visit <span class="visuallyHidden">Leicester City </span>Club Page<span class="icn arrow-right-w"></span></a>
</div>
</div>
<div class="teamPerformanceStandingsArea" style="display:none;">
<header>
<h3 class="subHeader left">Performance Chart</h3>
<a class="btn right" href="/stats/comparison">Compare against another team<span class="icn arrow-right"></span></a>
</header>
<div class="teamPerformanceStandingsContainer"></div>
</div>
</td>
</tr>
<tr class="" data-compseason="35" data-filtered-entry-size="8" data-filtered-table-row="308" data-filtered-table-row-abbr="308" data-filtered-table-row-name="Aston Villa" data-filtered-table-row-opta="t7605">
<td class="pos" tabindex="0">
<span class="value">4</span>
</td>
<td class="team" scope="row">
<a href="/clubs/2/Aston-Villa/overview"><span alt="" class="badge-25 t7605"></span><span class="long">Aston Villa</span><span class="short">AVL</span></a>
</td>
<td>7</td>
<td>3</td>
<td>3</td>
<td>1</td>
<td class="hideSmall">11</td>
<td class="hideSmall">9</td>
<td> 
        +2

 </td>
<td class="points">12</td>
<td class="form hideMed">
<ul>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12060" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 12 March 2016</span>
<span class="teamName">WOL</span>
<span class="badge-20 t6746"></span>
<span class="score">1 <span>-</span>2</span>
<span class="badge-20 t7605"></span>
<span class="teamName">AVL</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12061" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 19 March 2016</span>
<span class="teamName">AVL</span>
<span class="badge-20 t7605"></span>
<span class="score">0 <span>-</span>1</span>
<span class="badge-20 t6756"></span>
<span class="teamName">SUN</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12074" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 9 April 2016</span>
<span class="teamName">AVL</span>
<span class="badge-20 t7605"></span>
<span class="score">2 <span>-</span>1</span>
<span class="badge-20 t6753"></span>
<span class="teamName">WBA</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12088" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 16 April 2016</span>
<span class="teamName">TOT</span>
<span class="badge-20 t7631"></span>
<span class="score">0 <span>-</span>1</span>
<span class="badge-20 t7605"></span>
<span class="teamName">AVL</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="draw button-tooltip" id="Tooltip" role="tooltip" tabindex="0">D
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12101" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 30 April 2016</span>
<span class="teamName">AVL</span>
<span class="badge-20 t7605"></span>
<span class="score">1 <span>-</span>1</span>
<span class="badge-20 t8879"></span>
<span class="teamName">LEI</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
</ul>
<td class="nextMatchCol hideMed">
</td>
</td>
</tr>
<tr class="expandable" data-filtered-table-row-expander="308">
<td colspan="13">
<a class="expandableTeam" href="/clubs/2/Aston-Villa/overview">
<span class="badge-50 t7605"></span>
<span class="teamName">Aston Villa</span>
</a>
<div class="expandableFixtures">
<div class="resultWidget">
<div class="label"><strong>Recent Result</strong> - Saturday 12 March 2016</div>
<a class="matchAbridged pre" href="/match/12101">
<span class="teamName">AVL</span>
<span class="badge-20 t7605"></span>
<span class="score">1 <span>-</span>1</span>
<span class="badge-20 t8879"></span>
<span class="teamName">LEI</span>
<span class="icn arrow-right"></span>
</a>
</div>
<div class="btnContainer">
<a class="btn-highlight" href="/clubs/2/Aston-Villa/overview" role="btn">Visit <span class="visuallyHidden">Aston Villa </span>Club Page<span class="icn arrow-right-w"></span></a>
</div>
</div>
<div class="teamPerformanceStandingsArea" style="display:none;">
<header>
<h3 class="subHeader left">Performance Chart</h3>
<a class="btn right" href="/stats/comparison">Compare against another team<span class="icn arrow-right"></span></a>
</header>
<div class="teamPerformanceStandingsContainer"></div>
</div>
</td>
</tr>
<tr class="" data-compseason="35" data-filtered-entry-size="8" data-filtered-table-row="307" data-filtered-table-row-abbr="307" data-filtered-table-row-name="Arsenal" data-filtered-table-row-opta="t7606">
<td class="pos" tabindex="0">
<span class="value">5</span>
</td>
<td class="team" scope="row">
<a href="/clubs/1/Arsenal/overview"><span alt="" class="badge-25 t7606"></span><span class="long">Arsenal</span><span class="short">ARS</span></a>
</td>
<td>7</td>
<td>2</td>
<td>2</td>
<td>3</td>
<td class="hideSmall">15</td>
<td class="hideSmall">14</td>
<td> 
        +1

 </td>
<td class="points">8</td>
<td class="form hideMed">
<ul>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12059" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 12 March 2016</span>
<span class="teamName">WBA</span>
<span class="badge-20 t6753"></span>
<span class="score">2 <span>-</span>1</span>
<span class="badge-20 t7606"></span>
<span class="teamName">ARS</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12073" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 9 April 2016</span>
<span class="teamName">ARS</span>
<span class="badge-20 t7606"></span>
<span class="score">2 <span>-</span>1</span>
<span class="badge-20 t6746"></span>
<span class="teamName">WOL</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12083" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 16 April 2016</span>
<span class="teamName">ARS</span>
<span class="badge-20 t7606"></span>
<span class="score">1 <span>-</span>2</span>
<span class="badge-20 t8879"></span>
<span class="teamName">LEI</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12096" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 23 April 2016</span>
<span class="teamName">SUN</span>
<span class="badge-20 t6756"></span>
<span class="score">1 <span>-</span>4</span>
<span class="badge-20 t7606"></span>
<span class="teamName">ARS</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="draw button-tooltip" id="Tooltip" role="tooltip" tabindex="0">D
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12100" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 30 April 2016</span>
<span class="teamName">ARS</span>
<span class="badge-20 t7606"></span>
<span class="score">3 <span>-</span>3</span>
<span class="badge-20 t7631"></span>
<span class="teamName">TOT</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
</ul>
<td class="nextMatchCol hideMed">
</td>
</td>
</tr>
<tr class="expandable" data-filtered-table-row-expander="307">
<td colspan="13">
<a class="expandableTeam" href="/clubs/1/Arsenal/overview">
<span class="badge-50 t7606"></span>
<span class="teamName">Arsenal</span>
</a>
<div class="expandableFixtures">
<div class="resultWidget">
<div class="label"><strong>Recent Result</strong> - Saturday 12 March 2016</div>
<a class="matchAbridged pre" href="/match/12100">
<span class="teamName">ARS</span>
<span class="badge-20 t7606"></span>
<span class="score">3 <span>-</span>3</span>
<span class="badge-20 t7631"></span>
<span class="teamName">TOT</span>
<span class="icn arrow-right"></span>
</a>
</div>
<div class="btnContainer">
<a class="btn-highlight" href="/clubs/1/Arsenal/overview" role="btn">Visit <span class="visuallyHidden">Arsenal </span>Club Page<span class="icn arrow-right-w"></span></a>
</div>
</div>
<div class="teamPerformanceStandingsArea" style="display:none;">
<header>
<h3 class="subHeader left">Performance Chart</h3>
<a class="btn right" href="/stats/comparison">Compare against another team<span class="icn arrow-right"></span></a>
</header>
<div class="teamPerformanceStandingsContainer"></div>
</div>
</td>
</tr>
<tr class="" data-compseason="35" data-filtered-entry-size="8" data-filtered-table-row="327" data-filtered-table-row-abbr="327" data-filtered-table-row-name="Spurs" data-filtered-table-row-opta="t7631">
<td class="pos" tabindex="0">
<span class="value">6</span>
</td>
<td class="team" scope="row">
<a href="/clubs/21/Tottenham-Hotspur/overview"><span alt="" class="badge-25 t7631"></span><span class="long">Tottenham Hotspur</span><span class="short">TOT</span></a>
</td>
<td>7</td>
<td>2</td>
<td>1</td>
<td>4</td>
<td class="hideSmall">15</td>
<td class="hideSmall">17</td>
<td> 
        -2

 </td>
<td class="points">7</td>
<td class="form hideMed">
<ul>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12058" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 12 March 2016</span>
<span class="teamName">SUN</span>
<span class="badge-20 t6756"></span>
<span class="score">3 <span>-</span>0</span>
<span class="badge-20 t7631"></span>
<span class="teamName">TOT</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12067" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 19 March 2016</span>
<span class="teamName">TOT</span>
<span class="badge-20 t7631"></span>
<span class="score">7 <span>-</span>3</span>
<span class="badge-20 t6746"></span>
<span class="teamName">WOL</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12080" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 9 April 2016</span>
<span class="teamName">MID</span>
<span class="badge-20 t7143"></span>
<span class="score">1 <span>-</span>0</span>
<span class="badge-20 t7631"></span>
<span class="teamName">TOT</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12088" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 16 April 2016</span>
<span class="teamName">TOT</span>
<span class="badge-20 t7631"></span>
<span class="score">0 <span>-</span>1</span>
<span class="badge-20 t7605"></span>
<span class="teamName">AVL</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="draw button-tooltip" id="Tooltip" role="tooltip" tabindex="0">D
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12100" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 30 April 2016</span>
<span class="teamName">ARS</span>
<span class="badge-20 t7606"></span>
<span class="score">3 <span>-</span>3</span>
<span class="badge-20 t7631"></span>
<span class="teamName">TOT</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
</ul>
<td class="nextMatchCol hideMed">
</td>
</td>
</tr>
<tr class="expandable" data-filtered-table-row-expander="327">
<td colspan="13">
<a class="expandableTeam" href="/clubs/21/Tottenham-Hotspur/overview">
<span class="badge-50 t7631"></span>
<span class="teamName">Tottenham Hotspur</span>
</a>
<div class="expandableFixtures">
<div class="resultWidget">
<div class="label"><strong>Recent Result</strong> - Saturday 12 March 2016</div>
<a class="matchAbridged pre" href="/match/12100">
<span class="teamName">ARS</span>
<span class="badge-20 t7606"></span>
<span class="score">3 <span>-</span>3</span>
<span class="badge-20 t7631"></span>
<span class="teamName">TOT</span>
<span class="icn arrow-right"></span>
</a>
</div>
<div class="btnContainer">
<a class="btn-highlight" href="/clubs/21/Tottenham-Hotspur/overview" role="btn">Visit <span class="visuallyHidden">Tottenham Hotspur </span>Club Page<span class="icn arrow-right-w"></span></a>
</div>
</div>
<div class="teamPerformanceStandingsArea" style="display:none;">
<header>
<h3 class="subHeader left">Performance Chart</h3>
<a class="btn right" href="/stats/comparison">Compare against another team<span class="icn arrow-right"></span></a>
</header>
<div class="teamPerformanceStandingsContainer"></div>
</div>
</td>
</tr>
<tr class="" data-compseason="35" data-filtered-entry-size="8" data-filtered-table-row="328" data-filtered-table-row-abbr="328" data-filtered-table-row-name="West Brom" data-filtered-table-row-opta="t6753">
<td class="pos" tabindex="0">
<span class="value">7</span>
</td>
<td class="team" scope="row">
<a href="/clubs/36/West-Bromwich-Albion/overview"><span alt="" class="badge-25 t6753"></span><span class="long">West Bromwich Albion</span><span class="short">WBA</span></a>
</td>
<td>7</td>
<td>1</td>
<td>2</td>
<td>4</td>
<td class="hideSmall">8</td>
<td class="hideSmall">13</td>
<td> 
        -5

 </td>
<td class="points">5</td>
<td class="form hideMed">
<ul>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12059" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 12 March 2016</span>
<span class="teamName">WBA</span>
<span class="badge-20 t6753"></span>
<span class="score">2 <span>-</span>1</span>
<span class="badge-20 t7606"></span>
<span class="teamName">ARS</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="draw button-tooltip" id="Tooltip" role="tooltip" tabindex="0">D
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12064" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 19 March 2016</span>
<span class="teamName">LEI</span>
<span class="badge-20 t8879"></span>
<span class="score">1 <span>-</span>1</span>
<span class="badge-20 t6753"></span>
<span class="teamName">WBA</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12074" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 9 April 2016</span>
<span class="teamName">AVL</span>
<span class="badge-20 t7605"></span>
<span class="score">2 <span>-</span>1</span>
<span class="badge-20 t6753"></span>
<span class="teamName">WBA</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12089" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 16 April 2016</span>
<span class="teamName">WBA</span>
<span class="badge-20 t6753"></span>
<span class="score">1 <span>-</span>4</span>
<span class="badge-20 t6756"></span>
<span class="teamName">SUN</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12107" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 30 April 2016</span>
<span class="teamName">MID</span>
<span class="badge-20 t7143"></span>
<span class="score">1 <span>-</span>0</span>
<span class="badge-20 t6753"></span>
<span class="teamName">WBA</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
</ul>
<td class="nextMatchCol hideMed">
</td>
</td>
</tr>
<tr class="expandable" data-filtered-table-row-expander="328">
<td colspan="13">
<a class="expandableTeam" href="/clubs/36/West-Bromwich-Albion/overview">
<span class="badge-50 t6753"></span>
<span class="teamName">West Bromwich Albion</span>
</a>
<div class="expandableFixtures">
<div class="resultWidget">
<div class="label"><strong>Recent Result</strong> - Saturday 12 March 2016</div>
<a class="matchAbridged pre" href="/match/12107">
<span class="teamName">MID</span>
<span class="badge-20 t7143"></span>
<span class="score">1 <span>-</span>0</span>
<span class="badge-20 t6753"></span>
<span class="teamName">WBA</span>
<span class="icn arrow-right"></span>
</a>
</div>
<div class="btnContainer">
<a class="btn-highlight" href="/clubs/36/West-Bromwich-Albion/overview" role="btn">Visit <span class="visuallyHidden">West Bromwich Albion </span>Club Page<span class="icn arrow-right-w"></span></a>
</div>
</div>
<div class="teamPerformanceStandingsArea" style="display:none;">
<header>
<h3 class="subHeader left">Performance Chart</h3>
<a class="btn right" href="/stats/comparison">Compare against another team<span class="icn arrow-right"></span></a>
</header>
<div class="teamPerformanceStandingsContainer"></div>
</div>
</td>
</tr>
<tr class="" data-compseason="35" data-filtered-entry-size="8" data-filtered-table-row="330" data-filtered-table-row-abbr="330" data-filtered-table-row-name="Wolves" data-filtered-table-row-opta="t6746">
<td class="pos" tabindex="0">
<span class="value">8</span>
</td>
<td class="team" scope="row">
<a href="/clubs/38/Wolverhampton-Wanderers/overview"><span alt="" class="badge-25 t6746"></span><span class="long">Wolverhampton Wanderers</span><span class="short">WOL</span></a>
</td>
<td>7</td>
<td>0</td>
<td>1</td>
<td>6</td>
<td class="hideSmall">10</td>
<td class="hideSmall">25</td>
<td> 
        -15

 </td>
<td class="points">1</td>
<td class="form hideMed">
<ul>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12060" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 12 March 2016</span>
<span class="teamName">WOL</span>
<span class="badge-20 t6746"></span>
<span class="score">1 <span>-</span>2</span>
<span class="badge-20 t7605"></span>
<span class="teamName">AVL</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12067" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 19 March 2016</span>
<span class="teamName">TOT</span>
<span class="badge-20 t7631"></span>
<span class="score">7 <span>-</span>3</span>
<span class="badge-20 t6746"></span>
<span class="teamName">WOL</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12073" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 9 April 2016</span>
<span class="teamName">ARS</span>
<span class="badge-20 t7606"></span>
<span class="score">2 <span>-</span>1</span>
<span class="badge-20 t6746"></span>
<span class="teamName">WOL</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12091" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 16 April 2016</span>
<span class="teamName">WOL</span>
<span class="badge-20 t6746"></span>
<span class="score">2 <span>-</span>3</span>
<span class="badge-20 t7143"></span>
<span class="teamName">MID</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12109" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 30 April 2016</span>
<span class="teamName">SUN</span>
<span class="badge-20 t6756"></span>
<span class="score">4 <span>-</span>1</span>
<span class="badge-20 t6746"></span>
<span class="teamName">WOL</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
</ul>
<td class="nextMatchCol hideMed">
</td>
</td>
</tr>
<tr class="expandable" data-filtered-table-row-expander="330">
<td colspan="13">
<a class="expandableTeam" href="/clubs/38/Wolverhampton-Wanderers/overview">
<span class="badge-50 t6746"></span>
<span class="teamName">Wolverhampton Wanderers</span>
</a>
<div class="expandableFixtures">
<div class="resultWidget">
<div class="label"><strong>Recent Result</strong> - Saturday 12 March 2016</div>
<a class="matchAbridged pre" href="/match/12109">
<span class="teamName">SUN</span>
<span class="badge-20 t6756"></span>
<span class="score">4 <span>-</span>1</span>
<span class="badge-20 t6746"></span>
<span class="teamName">WOL</span>
<span class="icn arrow-right"></span>
</a>
</div>
<div class="btnContainer">
<a class="btn-highlight" href="/clubs/38/Wolverhampton-Wanderers/overview" role="btn">Visit <span class="visuallyHidden">Wolverhampton Wanderers </span>Club Page<span class="icn arrow-right-w"></span></a>
</div>
</div>
<div class="teamPerformanceStandingsArea" style="display:none;">
<header>
<h3 class="subHeader left">Performance Chart</h3>
<a class="btn right" href="/stats/comparison">Compare against another team<span class="icn arrow-right"></span></a>
</header>
<div class="teamPerformanceStandingsContainer"></div>
</div>
</td>
</tr>
</tbody>
</table>
</div>, <div class="table wrapper col-12">
<table>
<summary class="visuallyHidden">This table charts the Premier League teams</summary>
<thead>
<tr>
<th class="text-centre" scope="col">
<div class="thFull">Position</div>
<div class="thShort">Pos</div>
</th>
<th class="team" scope="col">Club</th>
<th scope="col">
<div class="thFull">Played</div>
<div class="thShort">Pl</div>
</th>
<th scope="col">
<div class="thFull">Won</div>
<div class="thShort">W</div>
</th>
<th scope="col">
<div class="thFull">Drawn</div>
<div class="thShort">D</div>
</th>
<th scope="col">
<div class="thFull">Lost</div>
<div class="thShort">L</div>
</th>
<th class="hideSmall" scope="col"><abbr title="Goals For">GF</abbr></th>
<th class="hideSmall" scope="col"><abbr title="Goals Against">GA</abbr></th>
<th scope="col"><abbr title="Goal Difference">GD</abbr></th>
<th class="points" scope="col">
<div class="thFull">Points</div>
<div class="thShort">Pts</div>
</th>
<th class="teamForm hideMed" scope="col">Form</th>
<th class="hideMed text-centre" scope="col">Next</th>
</tr>
</thead>
<tbody class="tableBodyContainer">
<tr class="tableDark" data-compseason="35" data-filtered-entry-size="8" data-filtered-table-row="326" data-filtered-table-row-abbr="326" data-filtered-table-row-name="Swansea" data-filtered-table-row-opta="t8967">
<td class="pos" tabindex="0">
<span class="value">1</span>
</td>
<td class="team" scope="row">
<a href="/clubs/45/Swansea-City/overview"><span alt="" class="badge-25 t8967"></span><span class="long">Swansea City</span><span class="short">SWA</span></a>
</td>
<td>7</td>
<td>4</td>
<td>3</td>
<td>0</td>
<td class="hideSmall">17</td>
<td class="hideSmall">13</td>
<td> 
        +4

 </td>
<td class="points">15</td>
<td class="form hideMed">
<ul>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12055" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 12 March 2016</span>
<span class="teamName">NOR</span>
<span class="badge-20 t7604"></span>
<span class="score">0 <span>-</span>1</span>
<span class="badge-20 t8967"></span>
<span class="teamName">SWA</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12082" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 9 April 2016</span>
<span class="teamName">SWA</span>
<span class="badge-20 t8967"></span>
<span class="score">2 <span>-</span>1</span>
<span class="badge-20 t6747"></span>
<span class="teamName">STK</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12084" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 16 April 2016</span>
<span class="teamName">DER</span>
<span class="badge-20 t6757"></span>
<span class="score">3 <span>-</span>4</span>
<span class="badge-20 t8967"></span>
<span class="teamName">SWA</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="draw button-tooltip" id="Tooltip" role="tooltip" tabindex="0">D
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12094" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 23 April 2016</span>
<span class="teamName">BHA</span>
<span class="badge-20 t7552"></span>
<span class="score">3 <span>-</span>3</span>
<span class="badge-20 t8967"></span>
<span class="teamName">SWA</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12110" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 30 April 2016</span>
<span class="teamName">SWA</span>
<span class="badge-20 t8967"></span>
<span class="score">2 <span>-</span>1</span>
<span class="badge-20 t7603"></span>
<span class="teamName">NEW</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
</ul>
<td class="nextMatchCol hideMed">
</td>
</td>
</tr>
<tr class="expandable" data-filtered-table-row-expander="326">
<td colspan="13">
<a class="expandableTeam" href="/clubs/45/Swansea-City/overview">
<span class="badge-50 t8967"></span>
<span class="teamName">Swansea City</span>
</a>
<div class="expandableFixtures">
<div class="resultWidget">
<div class="label"><strong>Recent Result</strong> - Saturday 12 March 2016</div>
<a class="matchAbridged pre" href="/match/12110">
<span class="teamName">SWA</span>
<span class="badge-20 t8967"></span>
<span class="score">2 <span>-</span>1</span>
<span class="badge-20 t7603"></span>
<span class="teamName">NEW</span>
<span class="icn arrow-right"></span>
</a>
</div>
<div class="btnContainer">
<a class="btn-highlight" href="/clubs/45/Swansea-City/overview" role="btn">Visit <span class="visuallyHidden">Swansea City </span>Club Page<span class="icn arrow-right-w"></span></a>
</div>
</div>
<div class="teamPerformanceStandingsArea" style="display:none;">
<header>
<h3 class="subHeader left">Performance Chart</h3>
<a class="btn right" href="/stats/comparison">Compare against another team<span class="icn arrow-right"></span></a>
</header>
<div class="teamPerformanceStandingsContainer"></div>
</div>
</td>
</tr>
<tr class="" data-compseason="35" data-filtered-entry-size="8" data-filtered-table-row="310" data-filtered-table-row-abbr="310" data-filtered-table-row-name="Brighton" data-filtered-table-row-opta="t7552">
<td class="pos" tabindex="0">
<span class="value">2</span>
</td>
<td class="team" scope="row">
<a href="/clubs/131/Brighton-and-Hove-Albion/overview"><span alt="" class="badge-25 t7552"></span><span class="long">Brighton and Hove Albion</span><span class="short">BHA</span></a>
</td>
<td>7</td>
<td>4</td>
<td>2</td>
<td>1</td>
<td class="hideSmall">18</td>
<td class="hideSmall">13</td>
<td> 
        +5

 </td>
<td class="points">14</td>
<td class="form hideMed">
<ul>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12051" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Friday 11 March 2016</span>
<span class="teamName">MUN</span>
<span class="badge-20 t6752"></span>
<span class="score">1 <span>-</span>2</span>
<span class="badge-20 t7552"></span>
<span class="teamName">BHA</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12071" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 2 April 2016</span>
<span class="teamName">NEW</span>
<span class="badge-20 t7603"></span>
<span class="score">2 <span>-</span>1</span>
<span class="badge-20 t7552"></span>
<span class="teamName">BHA</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12075" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 9 April 2016</span>
<span class="teamName">BHA</span>
<span class="badge-20 t7552"></span>
<span class="score">2 <span>-</span>1</span>
<span class="badge-20 t6757"></span>
<span class="teamName">DER</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="draw button-tooltip" id="Tooltip" role="tooltip" tabindex="0">D
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12094" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 23 April 2016</span>
<span class="teamName">BHA</span>
<span class="badge-20 t7552"></span>
<span class="score">3 <span>-</span>3</span>
<span class="badge-20 t8967"></span>
<span class="teamName">SWA</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12102" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 30 April 2016</span>
<span class="teamName">BHA</span>
<span class="badge-20 t7552"></span>
<span class="score">2 <span>-</span>1</span>
<span class="badge-20 t6747"></span>
<span class="teamName">STK</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
</ul>
<td class="nextMatchCol hideMed">
</td>
</td>
</tr>
<tr class="expandable" data-filtered-table-row-expander="310">
<td colspan="13">
<a class="expandableTeam" href="/clubs/131/Brighton-and-Hove-Albion/overview">
<span class="badge-50 t7552"></span>
<span class="teamName">Brighton and Hove Albion</span>
</a>
<div class="expandableFixtures">
<div class="resultWidget">
<div class="label"><strong>Recent Result</strong> - Friday 11 March 2016</div>
<a class="matchAbridged pre" href="/match/12102">
<span class="teamName">BHA</span>
<span class="badge-20 t7552"></span>
<span class="score">2 <span>-</span>1</span>
<span class="badge-20 t6747"></span>
<span class="teamName">STK</span>
<span class="icn arrow-right"></span>
</a>
</div>
<div class="btnContainer">
<a class="btn-highlight" href="/clubs/131/Brighton-and-Hove-Albion/overview" role="btn">Visit <span class="visuallyHidden">Brighton and Hove Albion </span>Club Page<span class="icn arrow-right-w"></span></a>
</div>
</div>
<div class="teamPerformanceStandingsArea" style="display:none;">
<header>
<h3 class="subHeader left">Performance Chart</h3>
<a class="btn right" href="/stats/comparison">Compare against another team<span class="icn arrow-right"></span></a>
</header>
<div class="teamPerformanceStandingsContainer"></div>
</div>
</td>
</tr>
<tr class="" data-compseason="35" data-filtered-entry-size="8" data-filtered-table-row="312" data-filtered-table-row-abbr="312" data-filtered-table-row-name="Derby" data-filtered-table-row-opta="t6757">
<td class="pos" tabindex="0">
<span class="value">3</span>
</td>
<td class="team" scope="row">
<a href="/clubs/28/Derby-County/overview"><span alt="" class="badge-25 t6757"></span><span class="long">Derby County</span><span class="short">DER</span></a>
</td>
<td>7</td>
<td>4</td>
<td>1</td>
<td>2</td>
<td class="hideSmall">17</td>
<td class="hideSmall">10</td>
<td> 
        +7

 </td>
<td class="points">13</td>
<td class="form hideMed">
<ul>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12063" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 19 March 2016</span>
<span class="teamName">DER</span>
<span class="badge-20 t6757"></span>
<span class="score">3 <span>-</span>0</span>
<span class="badge-20 t6752"></span>
<span class="teamName">MUN</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12075" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 9 April 2016</span>
<span class="teamName">BHA</span>
<span class="badge-20 t7552"></span>
<span class="score">2 <span>-</span>1</span>
<span class="badge-20 t6757"></span>
<span class="teamName">DER</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12084" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 16 April 2016</span>
<span class="teamName">DER</span>
<span class="badge-20 t6757"></span>
<span class="score">3 <span>-</span>4</span>
<span class="badge-20 t8967"></span>
<span class="teamName">SWA</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12093" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Friday 22 April 2016</span>
<span class="teamName">SOU</span>
<span class="badge-20 t7588"></span>
<span class="score">0 <span>-</span>1</span>
<span class="badge-20 t6757"></span>
<span class="teamName">DER</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12103" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 30 April 2016</span>
<span class="teamName">DER</span>
<span class="badge-20 t6757"></span>
<span class="score">2 <span>-</span>1</span>
<span class="badge-20 t7604"></span>
<span class="teamName">NOR</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
</ul>
<td class="nextMatchCol hideMed">
</td>
</td>
</tr>
<tr class="expandable" data-filtered-table-row-expander="312">
<td colspan="13">
<a class="expandableTeam" href="/clubs/28/Derby-County/overview">
<span class="badge-50 t6757"></span>
<span class="teamName">Derby County</span>
</a>
<div class="expandableFixtures">
<div class="resultWidget">
<div class="label"><strong>Recent Result</strong> - Saturday 19 March 2016</div>
<a class="matchAbridged pre" href="/match/12103">
<span class="teamName">DER</span>
<span class="badge-20 t6757"></span>
<span class="score">2 <span>-</span>1</span>
<span class="badge-20 t7604"></span>
<span class="teamName">NOR</span>
<span class="icn arrow-right"></span>
</a>
</div>
<div class="btnContainer">
<a class="btn-highlight" href="/clubs/28/Derby-County/overview" role="btn">Visit <span class="visuallyHidden">Derby County </span>Club Page<span class="icn arrow-right-w"></span></a>
</div>
</div>
<div class="teamPerformanceStandingsArea" style="display:none;">
<header>
<h3 class="subHeader left">Performance Chart</h3>
<a class="btn right" href="/stats/comparison">Compare against another team<span class="icn arrow-right"></span></a>
</header>
<div class="teamPerformanceStandingsContainer"></div>
</div>
</td>
</tr>
<tr class="" data-compseason="35" data-filtered-entry-size="8" data-filtered-table-row="318" data-filtered-table-row-abbr="318" data-filtered-table-row-name="Manchester United" data-filtered-table-row-opta="t6752">
<td class="pos" tabindex="0">
<span class="value">4</span>
</td>
<td class="team" scope="row">
<a href="/clubs/12/Manchester-United/overview"><span alt="" class="badge-25 t6752"></span><span class="long">Manchester United</span><span class="short">MUN</span></a>
</td>
<td>7</td>
<td>4</td>
<td>1</td>
<td>2</td>
<td class="hideSmall">17</td>
<td class="hideSmall">12</td>
<td> 
        +5

 </td>
<td class="points">13</td>
<td class="form hideMed">
<ul>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12051" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Friday 11 March 2016</span>
<span class="teamName">MUN</span>
<span class="badge-20 t6752"></span>
<span class="score">1 <span>-</span>2</span>
<span class="badge-20 t7552"></span>
<span class="teamName">BHA</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12063" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 19 March 2016</span>
<span class="teamName">DER</span>
<span class="badge-20 t6757"></span>
<span class="score">3 <span>-</span>0</span>
<span class="badge-20 t6752"></span>
<span class="teamName">MUN</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12079" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 9 April 2016</span>
<span class="teamName">MUN</span>
<span class="badge-20 t6752"></span>
<span class="score">7 <span>-</span>1</span>
<span class="badge-20 t7603"></span>
<span class="teamName">NEW</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12092" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Friday 22 April 2016</span>
<span class="teamName">NOR</span>
<span class="badge-20 t7604"></span>
<span class="score">2 <span>-</span>3</span>
<span class="badge-20 t6752"></span>
<span class="teamName">MUN</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12106" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 30 April 2016</span>
<span class="teamName">MUN</span>
<span class="badge-20 t6752"></span>
<span class="score">1 <span>-</span>0</span>
<span class="badge-20 t7588"></span>
<span class="teamName">SOU</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
</ul>
<td class="nextMatchCol hideMed">
</td>
</td>
</tr>
<tr class="expandable" data-filtered-table-row-expander="318">
<td colspan="13">
<a class="expandableTeam" href="/clubs/12/Manchester-United/overview">
<span class="badge-50 t6752"></span>
<span class="teamName">Manchester United</span>
</a>
<div class="expandableFixtures">
<div class="resultWidget">
<div class="label"><strong>Recent Result</strong> - Friday 11 March 2016</div>
<a class="matchAbridged pre" href="/match/12106">
<span class="teamName">MUN</span>
<span class="badge-20 t6752"></span>
<span class="score">1 <span>-</span>0</span>
<span class="badge-20 t7588"></span>
<span class="teamName">SOU</span>
<span class="icn arrow-right"></span>
</a>
</div>
<div class="btnContainer">
<a class="btn-highlight" href="/clubs/12/Manchester-United/overview" role="btn">Visit <span class="visuallyHidden">Manchester United </span>Club Page<span class="icn arrow-right-w"></span></a>
</div>
</div>
<div class="teamPerformanceStandingsArea" style="display:none;">
<header>
<h3 class="subHeader left">Performance Chart</h3>
<a class="btn right" href="/stats/comparison">Compare against another team<span class="icn arrow-right"></span></a>
</header>
<div class="teamPerformanceStandingsContainer"></div>
</div>
</td>
</tr>
<tr class="" data-compseason="35" data-filtered-entry-size="8" data-filtered-table-row="324" data-filtered-table-row-abbr="324" data-filtered-table-row-name="Stoke" data-filtered-table-row-opta="t6747">
<td class="pos" tabindex="0">
<span class="value">5</span>
</td>
<td class="team" scope="row">
<a href="/clubs/42/Stoke-City/overview"><span alt="" class="badge-25 t6747"></span><span class="long">Stoke City</span><span class="short">STK</span></a>
</td>
<td>7</td>
<td>3</td>
<td>1</td>
<td>3</td>
<td class="hideSmall">12</td>
<td class="hideSmall">12</td>
<td> 
        0

 </td>
<td class="points">10</td>
<td class="form hideMed">
<ul>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12057" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 12 March 2016</span>
<span class="teamName">STK</span>
<span class="badge-20 t6747"></span>
<span class="score">2 <span>-</span>1</span>
<span class="badge-20 t7603"></span>
<span class="teamName">NEW</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12066" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 19 March 2016</span>
<span class="teamName">NOR</span>
<span class="badge-20 t7604"></span>
<span class="score">2 <span>-</span>3</span>
<span class="badge-20 t6747"></span>
<span class="teamName">STK</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12082" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 9 April 2016</span>
<span class="teamName">SWA</span>
<span class="badge-20 t8967"></span>
<span class="score">2 <span>-</span>1</span>
<span class="badge-20 t6747"></span>
<span class="teamName">STK</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12087" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 16 April 2016</span>
<span class="teamName">STK</span>
<span class="badge-20 t6747"></span>
<span class="score">1 <span>-</span>0</span>
<span class="badge-20 t7588"></span>
<span class="teamName">SOU</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12102" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 30 April 2016</span>
<span class="teamName">BHA</span>
<span class="badge-20 t7552"></span>
<span class="score">2 <span>-</span>1</span>
<span class="badge-20 t6747"></span>
<span class="teamName">STK</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
</ul>
<td class="nextMatchCol hideMed">
</td>
</td>
</tr>
<tr class="expandable" data-filtered-table-row-expander="324">
<td colspan="13">
<a class="expandableTeam" href="/clubs/42/Stoke-City/overview">
<span class="badge-50 t6747"></span>
<span class="teamName">Stoke City</span>
</a>
<div class="expandableFixtures">
<div class="resultWidget">
<div class="label"><strong>Recent Result</strong> - Saturday 12 March 2016</div>
<a class="matchAbridged pre" href="/match/12102">
<span class="teamName">BHA</span>
<span class="badge-20 t7552"></span>
<span class="score">2 <span>-</span>1</span>
<span class="badge-20 t6747"></span>
<span class="teamName">STK</span>
<span class="icn arrow-right"></span>
</a>
</div>
<div class="btnContainer">
<a class="btn-highlight" href="/clubs/42/Stoke-City/overview" role="btn">Visit <span class="visuallyHidden">Stoke City </span>Club Page<span class="icn arrow-right-w"></span></a>
</div>
</div>
<div class="teamPerformanceStandingsArea" style="display:none;">
<header>
<h3 class="subHeader left">Performance Chart</h3>
<a class="btn right" href="/stats/comparison">Compare against another team<span class="icn arrow-right"></span></a>
</header>
<div class="teamPerformanceStandingsContainer"></div>
</div>
</td>
</tr>
<tr class="" data-compseason="35" data-filtered-entry-size="8" data-filtered-table-row="320" data-filtered-table-row-abbr="320" data-filtered-table-row-name="Newcastle United" data-filtered-table-row-opta="t7603">
<td class="pos" tabindex="0">
<span class="value">6</span>
</td>
<td class="team" scope="row">
<a href="/clubs/23/Newcastle-United/overview"><span alt="" class="badge-25 t7603"></span><span class="long">Newcastle United</span><span class="short">NEW</span></a>
</td>
<td>7</td>
<td>2</td>
<td>1</td>
<td>4</td>
<td class="hideSmall">10</td>
<td class="hideSmall">18</td>
<td> 
        -8

 </td>
<td class="points">7</td>
<td class="form hideMed">
<ul>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12057" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 12 March 2016</span>
<span class="teamName">STK</span>
<span class="badge-20 t6747"></span>
<span class="score">2 <span>-</span>1</span>
<span class="badge-20 t7603"></span>
<span class="teamName">NEW</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12071" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 2 April 2016</span>
<span class="teamName">NEW</span>
<span class="badge-20 t7603"></span>
<span class="score">2 <span>-</span>1</span>
<span class="badge-20 t7552"></span>
<span class="teamName">BHA</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12079" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 9 April 2016</span>
<span class="teamName">MUN</span>
<span class="badge-20 t6752"></span>
<span class="score">7 <span>-</span>1</span>
<span class="badge-20 t7603"></span>
<span class="teamName">NEW</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12110" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 30 April 2016</span>
<span class="teamName">SWA</span>
<span class="badge-20 t8967"></span>
<span class="score">2 <span>-</span>1</span>
<span class="badge-20 t7603"></span>
<span class="teamName">NEW</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12114" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 7 May 2016</span>
<span class="teamName">NEW</span>
<span class="badge-20 t7603"></span>
<span class="score">4 <span>-</span>1</span>
<span class="badge-20 t7588"></span>
<span class="teamName">SOU</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
</ul>
<td class="nextMatchCol hideMed">
</td>
</td>
</tr>
<tr class="expandable" data-filtered-table-row-expander="320">
<td colspan="13">
<a class="expandableTeam" href="/clubs/23/Newcastle-United/overview">
<span class="badge-50 t7603"></span>
<span class="teamName">Newcastle United</span>
</a>
<div class="expandableFixtures">
<div class="resultWidget">
<div class="label"><strong>Recent Result</strong> - Saturday 12 March 2016</div>
<a class="matchAbridged pre" href="/match/12114">
<span class="teamName">NEW</span>
<span class="badge-20 t7603"></span>
<span class="score">4 <span>-</span>1</span>
<span class="badge-20 t7588"></span>
<span class="teamName">SOU</span>
<span class="icn arrow-right"></span>
</a>
</div>
<div class="btnContainer">
<a class="btn-highlight" href="/clubs/23/Newcastle-United/overview" role="btn">Visit <span class="visuallyHidden">Newcastle United </span>Club Page<span class="icn arrow-right-w"></span></a>
</div>
</div>
<div class="teamPerformanceStandingsArea" style="display:none;">
<header>
<h3 class="subHeader left">Performance Chart</h3>
<a class="btn right" href="/stats/comparison">Compare against another team<span class="icn arrow-right"></span></a>
</header>
<div class="teamPerformanceStandingsContainer"></div>
</div>
</td>
</tr>
<tr class="" data-compseason="35" data-filtered-entry-size="8" data-filtered-table-row="323" data-filtered-table-row-abbr="323" data-filtered-table-row-name="Southampton" data-filtered-table-row-opta="t7588">
<td class="pos" tabindex="0">
<span class="value">7</span>
</td>
<td class="team" scope="row">
<a href="/clubs/20/Southampton/overview"><span alt="" class="badge-25 t7588"></span><span class="long">Southampton</span><span class="short">SOU</span></a>
</td>
<td>7</td>
<td>1</td>
<td>2</td>
<td>4</td>
<td class="hideSmall">9</td>
<td class="hideSmall">13</td>
<td> 
        -4

 </td>
<td class="points">5</td>
<td class="form hideMed">
<ul>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12081" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 9 April 2016</span>
<span class="teamName">SOU</span>
<span class="badge-20 t7588"></span>
<span class="score">3 <span>-</span>1</span>
<span class="badge-20 t7604"></span>
<span class="teamName">NOR</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12087" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 16 April 2016</span>
<span class="teamName">STK</span>
<span class="badge-20 t6747"></span>
<span class="score">1 <span>-</span>0</span>
<span class="badge-20 t7588"></span>
<span class="teamName">SOU</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12093" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Friday 22 April 2016</span>
<span class="teamName">SOU</span>
<span class="badge-20 t7588"></span>
<span class="score">0 <span>-</span>1</span>
<span class="badge-20 t6757"></span>
<span class="teamName">DER</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12106" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 30 April 2016</span>
<span class="teamName">MUN</span>
<span class="badge-20 t6752"></span>
<span class="score">1 <span>-</span>0</span>
<span class="badge-20 t7588"></span>
<span class="teamName">SOU</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12114" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 7 May 2016</span>
<span class="teamName">NEW</span>
<span class="badge-20 t7603"></span>
<span class="score">4 <span>-</span>1</span>
<span class="badge-20 t7588"></span>
<span class="teamName">SOU</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
</ul>
<td class="nextMatchCol hideMed">
</td>
</td>
</tr>
<tr class="expandable" data-filtered-table-row-expander="323">
<td colspan="13">
<a class="expandableTeam" href="/clubs/20/Southampton/overview">
<span class="badge-50 t7588"></span>
<span class="teamName">Southampton</span>
</a>
<div class="expandableFixtures">
<div class="resultWidget">
<div class="label"><strong>Recent Result</strong> - Saturday 9 April 2016</div>
<a class="matchAbridged pre" href="/match/12114">
<span class="teamName">NEW</span>
<span class="badge-20 t7603"></span>
<span class="score">4 <span>-</span>1</span>
<span class="badge-20 t7588"></span>
<span class="teamName">SOU</span>
<span class="icn arrow-right"></span>
</a>
</div>
<div class="btnContainer">
<a class="btn-highlight" href="/clubs/20/Southampton/overview" role="btn">Visit <span class="visuallyHidden">Southampton </span>Club Page<span class="icn arrow-right-w"></span></a>
</div>
</div>
<div class="teamPerformanceStandingsArea" style="display:none;">
<header>
<h3 class="subHeader left">Performance Chart</h3>
<a class="btn right" href="/stats/comparison">Compare against another team<span class="icn arrow-right"></span></a>
</header>
<div class="teamPerformanceStandingsContainer"></div>
</div>
</td>
</tr>
<tr class="" data-compseason="35" data-filtered-entry-size="8" data-filtered-table-row="321" data-filtered-table-row-abbr="321" data-filtered-table-row-name="Norwich" data-filtered-table-row-opta="t7604">
<td class="pos" tabindex="0">
<span class="value">8</span>
</td>
<td class="team" scope="row">
<a href="/clubs/14/Norwich-City/overview"><span alt="" class="badge-25 t7604"></span><span class="long">Norwich City</span><span class="short">NOR</span></a>
</td>
<td>7</td>
<td>0</td>
<td>1</td>
<td>6</td>
<td class="hideSmall">9</td>
<td class="hideSmall">18</td>
<td> 
        -9

 </td>
<td class="points">1</td>
<td class="form hideMed">
<ul>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12055" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 12 March 2016</span>
<span class="teamName">NOR</span>
<span class="badge-20 t7604"></span>
<span class="score">0 <span>-</span>1</span>
<span class="badge-20 t8967"></span>
<span class="teamName">SWA</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12066" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 19 March 2016</span>
<span class="teamName">NOR</span>
<span class="badge-20 t7604"></span>
<span class="score">2 <span>-</span>3</span>
<span class="badge-20 t6747"></span>
<span class="teamName">STK</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12081" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 9 April 2016</span>
<span class="teamName">SOU</span>
<span class="badge-20 t7588"></span>
<span class="score">3 <span>-</span>1</span>
<span class="badge-20 t7604"></span>
<span class="teamName">NOR</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12092" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Friday 22 April 2016</span>
<span class="teamName">NOR</span>
<span class="badge-20 t7604"></span>
<span class="score">2 <span>-</span>3</span>
<span class="badge-20 t6752"></span>
<span class="teamName">MUN</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12103" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 30 April 2016</span>
<span class="teamName">DER</span>
<span class="badge-20 t6757"></span>
<span class="score">2 <span>-</span>1</span>
<span class="badge-20 t7604"></span>
<span class="teamName">NOR</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
</ul>
<td class="nextMatchCol hideMed">
</td>
</td>
</tr>
<tr class="expandable" data-filtered-table-row-expander="321">
<td colspan="13">
<a class="expandableTeam" href="/clubs/14/Norwich-City/overview">
<span class="badge-50 t7604"></span>
<span class="teamName">Norwich City</span>
</a>
<div class="expandableFixtures">
<div class="resultWidget">
<div class="label"><strong>Recent Result</strong> - Saturday 12 March 2016</div>
<a class="matchAbridged pre" href="/match/12103">
<span class="teamName">DER</span>
<span class="badge-20 t6757"></span>
<span class="score">2 <span>-</span>1</span>
<span class="badge-20 t7604"></span>
<span class="teamName">NOR</span>
<span class="icn arrow-right"></span>
</a>
</div>
<div class="btnContainer">
<a class="btn-highlight" href="/clubs/14/Norwich-City/overview" role="btn">Visit <span class="visuallyHidden">Norwich City </span>Club Page<span class="icn arrow-right-w"></span></a>
</div>
</div>
<div class="teamPerformanceStandingsArea" style="display:none;">
<header>
<h3 class="subHeader left">Performance Chart</h3>
<a class="btn right" href="/stats/comparison">Compare against another team<span class="icn arrow-right"></span></a>
</header>
<div class="teamPerformanceStandingsContainer"></div>
</div>
</td>
</tr>
</tbody>
</table>
</div>, <div class="table wrapper col-12">
<table>
<summary class="visuallyHidden">This table charts the Premier League teams</summary>
<thead>
<tr>
<th class="text-centre" scope="col">
<div class="thFull">Position</div>
<div class="thShort">Pos</div>
</th>
<th class="team" scope="col">Club</th>
<th scope="col">
<div class="thFull">Played</div>
<div class="thShort">Pl</div>
</th>
<th scope="col">
<div class="thFull">Won</div>
<div class="thShort">W</div>
</th>
<th scope="col">
<div class="thFull">Drawn</div>
<div class="thShort">D</div>
</th>
<th scope="col">
<div class="thFull">Lost</div>
<div class="thShort">L</div>
</th>
<th class="hideSmall" scope="col"><abbr title="Goals For">GF</abbr></th>
<th class="hideSmall" scope="col"><abbr title="Goals Against">GA</abbr></th>
<th scope="col"><abbr title="Goal Difference">GD</abbr></th>
<th class="points" scope="col">
<div class="thFull">Points</div>
<div class="thShort">Pts</div>
</th>
<th class="teamForm hideMed" scope="col">Form</th>
<th class="hideMed text-centre" scope="col">Next</th>
</tr>
</thead>
<tbody class="tableBodyContainer">
<tr class="tableDark" data-compseason="35" data-filtered-entry-size="12" data-filtered-table-row="317" data-filtered-table-row-abbr="317" data-filtered-table-row-name="Manchester City" data-filtered-table-row-opta="t6718">
<td class="pos" tabindex="0">
<span class="value">1</span>
</td>
<td class="team" scope="row">
<a href="/clubs/11/Manchester-City/overview"><span alt="" class="badge-25 t6718"></span><span class="long">Manchester City</span><span class="short">MCI</span></a>
</td>
<td>22</td>
<td>14</td>
<td>6</td>
<td>2</td>
<td class="hideSmall">53</td>
<td class="hideSmall">23</td>
<td> 
        +30

 </td>
<td class="points">48</td>
<td class="form hideMed">
<ul>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12078" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 9 April 2016</span>
<span class="teamName">MCI</span>
<span class="badge-20 t6718"></span>
<span class="score">3 <span>-</span>0</span>
<span class="badge-20 t7632"></span>
<span class="teamName">WHU</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12086" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 16 April 2016</span>
<span class="teamName">LIV</span>
<span class="badge-20 t6717"></span>
<span class="score">0 <span>-</span>2</span>
<span class="badge-20 t6718"></span>
<span class="teamName">MCI</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12105" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 30 April 2016</span>
<span class="teamName">MCI</span>
<span class="badge-20 t6718"></span>
<span class="score">2 <span>-</span>0</span>
<span class="badge-20 t6748"></span>
<span class="teamName">BLB</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="draw button-tooltip" id="Tooltip" role="tooltip" tabindex="0">D
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12111" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Tuesday 3 May 2016</span>
<span class="teamName">EVE</span>
<span class="badge-20 t6749"></span>
<span class="score">4 <span>-</span>4</span>
<span class="badge-20 t6718"></span>
<span class="teamName">MCI</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12113" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 7 May 2016</span>
<span class="teamName">MCI</span>
<span class="badge-20 t6718"></span>
<span class="score">5 <span>-</span>0</span>
<span class="badge-20 t6886"></span>
<span class="teamName">FUL</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
</ul>
<td class="nextMatchCol hideMed">
</td>
</td>
</tr>
<tr class="expandable" data-filtered-table-row-expander="317">
<td colspan="13">
<a class="expandableTeam" href="/clubs/11/Manchester-City/overview">
<span class="badge-50 t6718"></span>
<span class="teamName">Manchester City</span>
</a>
<div class="expandableFixtures">
<div class="resultWidget">
<div class="label"><strong>Recent Result</strong> - Saturday 9 April 2016</div>
<a class="matchAbridged pre" href="/match/12113">
<span class="teamName">MCI</span>
<span class="badge-20 t6718"></span>
<span class="score">5 <span>-</span>0</span>
<span class="badge-20 t6886"></span>
<span class="teamName">FUL</span>
<span class="icn arrow-right"></span>
</a>
</div>
<div class="btnContainer">
<a class="btn-highlight" href="/clubs/11/Manchester-City/overview" role="btn">Visit <span class="visuallyHidden">Manchester City </span>Club Page<span class="icn arrow-right-w"></span></a>
</div>
</div>
<div class="teamPerformanceStandingsArea" style="display:none;">
<header>
<h3 class="subHeader left">Performance Chart</h3>
<a class="btn right" href="/stats/comparison">Compare against another team<span class="icn arrow-right"></span></a>
</header>
<div class="teamPerformanceStandingsContainer"></div>
</div>
</td>
</tr>
<tr class="" data-compseason="35" data-filtered-entry-size="12" data-filtered-table-row="313" data-filtered-table-row-abbr="313" data-filtered-table-row-name="Everton" data-filtered-table-row-opta="t6749">
<td class="pos" tabindex="0">
<span class="value">2</span>
</td>
<td class="team" scope="row">
<a href="/clubs/7/Everton/overview"><span alt="" class="badge-25 t6749"></span><span class="long">Everton</span><span class="short">EVE</span></a>
</td>
<td>22</td>
<td>15</td>
<td>3</td>
<td>4</td>
<td class="hideSmall">57</td>
<td class="hideSmall">33</td>
<td> 
        +24

 </td>
<td class="points">48</td>
<td class="form hideMed">
<ul>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12069" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 2 April 2016</span>
<span class="teamName">EVE</span>
<span class="badge-20 t6749"></span>
<span class="score">2 <span>-</span>1</span>
<span class="badge-20 t6748"></span>
<span class="teamName">BLB</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12076" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 9 April 2016</span>
<span class="teamName">EVE</span>
<span class="badge-20 t6749"></span>
<span class="score">0 <span>-</span>4</span>
<span class="badge-20 t6717"></span>
<span class="teamName">LIV</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12085" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 16 April 2016</span>
<span class="teamName">FUL</span>
<span class="badge-20 t6886"></span>
<span class="score">2 <span>-</span>3</span>
<span class="badge-20 t6749"></span>
<span class="teamName">EVE</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12104" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 30 April 2016</span>
<span class="teamName">EVE</span>
<span class="badge-20 t6749"></span>
<span class="score">4 <span>-</span>3</span>
<span class="badge-20 t7632"></span>
<span class="teamName">WHU</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="draw button-tooltip" id="Tooltip" role="tooltip" tabindex="0">D
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12111" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Tuesday 3 May 2016</span>
<span class="teamName">EVE</span>
<span class="badge-20 t6749"></span>
<span class="score">4 <span>-</span>4</span>
<span class="badge-20 t6718"></span>
<span class="teamName">MCI</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
</ul>
<td class="nextMatchCol hideMed">
</td>
</td>
</tr>
<tr class="expandable" data-filtered-table-row-expander="313">
<td colspan="13">
<a class="expandableTeam" href="/clubs/7/Everton/overview">
<span class="badge-50 t6749"></span>
<span class="teamName">Everton</span>
</a>
<div class="expandableFixtures">
<div class="resultWidget">
<div class="label"><strong>Recent Result</strong> - Saturday 2 April 2016</div>
<a class="matchAbridged pre" href="/match/12111">
<span class="teamName">EVE</span>
<span class="badge-20 t6749"></span>
<span class="score">4 <span>-</span>4</span>
<span class="badge-20 t6718"></span>
<span class="teamName">MCI</span>
<span class="icn arrow-right"></span>
</a>
</div>
<div class="btnContainer">
<a class="btn-highlight" href="/clubs/7/Everton/overview" role="btn">Visit <span class="visuallyHidden">Everton </span>Club Page<span class="icn arrow-right-w"></span></a>
</div>
</div>
<div class="teamPerformanceStandingsArea" style="display:none;">
<header>
<h3 class="subHeader left">Performance Chart</h3>
<a class="btn right" href="/stats/comparison">Compare against another team<span class="icn arrow-right"></span></a>
</header>
<div class="teamPerformanceStandingsContainer"></div>
</div>
</td>
</tr>
<tr class="" data-compseason="35" data-filtered-entry-size="12" data-filtered-table-row="316" data-filtered-table-row-abbr="316" data-filtered-table-row-name="Liverpool" data-filtered-table-row-opta="t6717">
<td class="pos" tabindex="0">
<span class="value">3</span>
</td>
<td class="team" scope="row">
<a href="/clubs/10/Liverpool/overview"><span alt="" class="badge-25 t6717"></span><span class="long">Liverpool</span><span class="short">LIV</span></a>
</td>
<td>22</td>
<td>13</td>
<td>4</td>
<td>5</td>
<td class="hideSmall">45</td>
<td class="hideSmall">28</td>
<td> 
        +17

 </td>
<td class="points">43</td>
<td class="form hideMed">
<ul>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12070" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 2 April 2016</span>
<span class="teamName">FUL</span>
<span class="badge-20 t6886"></span>
<span class="score">1 <span>-</span>5</span>
<span class="badge-20 t6717"></span>
<span class="teamName">LIV</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12076" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 9 April 2016</span>
<span class="teamName">EVE</span>
<span class="badge-20 t6749"></span>
<span class="score">0 <span>-</span>4</span>
<span class="badge-20 t6717"></span>
<span class="teamName">LIV</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12086" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 16 April 2016</span>
<span class="teamName">LIV</span>
<span class="badge-20 t6717"></span>
<span class="score">0 <span>-</span>2</span>
<span class="badge-20 t6718"></span>
<span class="teamName">MCI</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="draw button-tooltip" id="Tooltip" role="tooltip" tabindex="0">D
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12097" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 23 April 2016</span>
<span class="teamName">WHU</span>
<span class="badge-20 t7632"></span>
<span class="score">0 <span>-</span>0</span>
<span class="badge-20 t6717"></span>
<span class="teamName">LIV</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="draw button-tooltip" id="Tooltip" role="tooltip" tabindex="0">D
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12099" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Friday 29 April 2016</span>
<span class="teamName">CHE</span>
<span class="badge-20 t7141"></span>
<span class="score">2 <span>-</span>2</span>
<span class="badge-20 t6717"></span>
<span class="teamName">LIV</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
</ul>
<td class="nextMatchCol hideMed">
</td>
</td>
</tr>
<tr class="expandable" data-filtered-table-row-expander="316">
<td colspan="13">
<a class="expandableTeam" href="/clubs/10/Liverpool/overview">
<span class="badge-50 t6717"></span>
<span class="teamName">Liverpool</span>
</a>
<div class="expandableFixtures">
<div class="resultWidget">
<div class="label"><strong>Recent Result</strong> - Saturday 2 April 2016</div>
<a class="matchAbridged pre" href="/match/12099">
<span class="teamName">CHE</span>
<span class="badge-20 t7141"></span>
<span class="score">2 <span>-</span>2</span>
<span class="badge-20 t6717"></span>
<span class="teamName">LIV</span>
<span class="icn arrow-right"></span>
</a>
</div>
<div class="btnContainer">
<a class="btn-highlight" href="/clubs/10/Liverpool/overview" role="btn">Visit <span class="visuallyHidden">Liverpool </span>Club Page<span class="icn arrow-right-w"></span></a>
</div>
</div>
<div class="teamPerformanceStandingsArea" style="display:none;">
<header>
<h3 class="subHeader left">Performance Chart</h3>
<a class="btn right" href="/stats/comparison">Compare against another team<span class="icn arrow-right"></span></a>
</header>
<div class="teamPerformanceStandingsContainer"></div>
</div>
</td>
</tr>
<tr class="" data-compseason="35" data-filtered-entry-size="12" data-filtered-table-row="309" data-filtered-table-row-abbr="309" data-filtered-table-row-name="Blackburn" data-filtered-table-row-opta="t6748">
<td class="pos" tabindex="0">
<span class="value">4</span>
</td>
<td class="team" scope="row">
<a href="/clubs/3/Blackburn-Rovers/overview"><span alt="" class="badge-25 t6748"></span><span class="long">Blackburn Rovers</span><span class="short">BLB</span></a>
</td>
<td>22</td>
<td>11</td>
<td>4</td>
<td>7</td>
<td class="hideSmall">45</td>
<td class="hideSmall">31</td>
<td> 
        +14

 </td>
<td class="points">37</td>
<td class="form hideMed">
<ul>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12069" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 2 April 2016</span>
<span class="teamName">EVE</span>
<span class="badge-20 t6749"></span>
<span class="score">2 <span>-</span>1</span>
<span class="badge-20 t6748"></span>
<span class="teamName">BLB</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="draw button-tooltip" id="Tooltip" role="tooltip" tabindex="0">D
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12095" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 23 April 2016</span>
<span class="teamName">RDG</span>
<span class="badge-20 t7587"></span>
<span class="score">1 <span>-</span>1</span>
<span class="badge-20 t6748"></span>
<span class="teamName">BLB</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="draw button-tooltip" id="Tooltip" role="tooltip" tabindex="0">D
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12098" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Wednesday 27 April 2016</span>
<span class="teamName">BLB</span>
<span class="badge-20 t6748"></span>
<span class="score">1 <span>-</span>1</span>
<span class="badge-20 t7632"></span>
<span class="teamName">WHU</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12105" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 30 April 2016</span>
<span class="teamName">MCI</span>
<span class="badge-20 t6718"></span>
<span class="score">2 <span>-</span>0</span>
<span class="badge-20 t6748"></span>
<span class="teamName">BLB</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12112" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 7 May 2016</span>
<span class="teamName">BLB</span>
<span class="badge-20 t6748"></span>
<span class="score">3 <span>-</span>0</span>
<span class="badge-20 t7141"></span>
<span class="teamName">CHE</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
</ul>
<td class="nextMatchCol hideMed">
</td>
</td>
</tr>
<tr class="expandable" data-filtered-table-row-expander="309">
<td colspan="13">
<a class="expandableTeam" href="/clubs/3/Blackburn-Rovers/overview">
<span class="badge-50 t6748"></span>
<span class="teamName">Blackburn Rovers</span>
</a>
<div class="expandableFixtures">
<div class="resultWidget">
<div class="label"><strong>Recent Result</strong> - Saturday 2 April 2016</div>
<a class="matchAbridged pre" href="/match/12112">
<span class="teamName">BLB</span>
<span class="badge-20 t6748"></span>
<span class="score">3 <span>-</span>0</span>
<span class="badge-20 t7141"></span>
<span class="teamName">CHE</span>
<span class="icn arrow-right"></span>
</a>
</div>
<div class="btnContainer">
<a class="btn-highlight" href="/clubs/3/Blackburn-Rovers/overview" role="btn">Visit <span class="visuallyHidden">Blackburn Rovers </span>Club Page<span class="icn arrow-right-w"></span></a>
</div>
</div>
<div class="teamPerformanceStandingsArea" style="display:none;">
<header>
<h3 class="subHeader left">Performance Chart</h3>
<a class="btn right" href="/stats/comparison">Compare against another team<span class="icn arrow-right"></span></a>
</header>
<div class="teamPerformanceStandingsContainer"></div>
</div>
</td>
</tr>
<tr class="" data-compseason="35" data-filtered-entry-size="12" data-filtered-table-row="325" data-filtered-table-row-abbr="325" data-filtered-table-row-name="Sunderland" data-filtered-table-row-opta="t6756">
<td class="pos" tabindex="0">
<span class="value">5</span>
</td>
<td class="team" scope="row">
<a href="/clubs/29/Sunderland/overview"><span alt="" class="badge-25 t6756"></span><span class="long">Sunderland</span><span class="short">SUN</span></a>
</td>
<td>22</td>
<td>11</td>
<td>3</td>
<td>8</td>
<td class="hideSmall">44</td>
<td class="hideSmall">40</td>
<td> 
        +4

 </td>
<td class="points">36</td>
<td class="form hideMed">
<ul>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12061" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 19 March 2016</span>
<span class="teamName">AVL</span>
<span class="badge-20 t7605"></span>
<span class="score">0 <span>-</span>1</span>
<span class="badge-20 t6756"></span>
<span class="teamName">SUN</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="draw button-tooltip" id="Tooltip" role="tooltip" tabindex="0">D
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12072" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Friday 8 April 2016</span>
<span class="teamName">SUN</span>
<span class="badge-20 t6756"></span>
<span class="score">1 <span>-</span>1</span>
<span class="badge-20 t8879"></span>
<span class="teamName">LEI</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12089" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 16 April 2016</span>
<span class="teamName">WBA</span>
<span class="badge-20 t6753"></span>
<span class="score">1 <span>-</span>4</span>
<span class="badge-20 t6756"></span>
<span class="teamName">SUN</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12096" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 23 April 2016</span>
<span class="teamName">SUN</span>
<span class="badge-20 t6756"></span>
<span class="score">1 <span>-</span>4</span>
<span class="badge-20 t7606"></span>
<span class="teamName">ARS</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12109" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 30 April 2016</span>
<span class="teamName">SUN</span>
<span class="badge-20 t6756"></span>
<span class="score">4 <span>-</span>1</span>
<span class="badge-20 t6746"></span>
<span class="teamName">WOL</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
</ul>
<td class="nextMatchCol hideMed">
</td>
</td>
</tr>
<tr class="expandable" data-filtered-table-row-expander="325">
<td colspan="13">
<a class="expandableTeam" href="/clubs/29/Sunderland/overview">
<span class="badge-50 t6756"></span>
<span class="teamName">Sunderland</span>
</a>
<div class="expandableFixtures">
<div class="resultWidget">
<div class="label"><strong>Recent Result</strong> - Saturday 19 March 2016</div>
<a class="matchAbridged pre" href="/match/12109">
<span class="teamName">SUN</span>
<span class="badge-20 t6756"></span>
<span class="score">4 <span>-</span>1</span>
<span class="badge-20 t6746"></span>
<span class="teamName">WOL</span>
<span class="icn arrow-right"></span>
</a>
</div>
<div class="btnContainer">
<a class="btn-highlight" href="/clubs/29/Sunderland/overview" role="btn">Visit <span class="visuallyHidden">Sunderland </span>Club Page<span class="icn arrow-right-w"></span></a>
</div>
</div>
<div class="teamPerformanceStandingsArea" style="display:none;">
<header>
<h3 class="subHeader left">Performance Chart</h3>
<a class="btn right" href="/stats/comparison">Compare against another team<span class="icn arrow-right"></span></a>
</header>
<div class="teamPerformanceStandingsContainer"></div>
</div>
</td>
</tr>
<tr class="" data-compseason="35" data-filtered-entry-size="12" data-filtered-table-row="319" data-filtered-table-row-abbr="319" data-filtered-table-row-name="Middlesbrough" data-filtered-table-row-opta="t7143">
<td class="pos" tabindex="0">
<span class="value">6</span>
</td>
<td class="team" scope="row">
<a href="/clubs/13/Middlesbrough/overview"><span alt="" class="badge-25 t7143"></span><span class="long">Middlesbrough</span><span class="short">MID</span></a>
</td>
<td>22</td>
<td>10</td>
<td>4</td>
<td>8</td>
<td class="hideSmall">43</td>
<td class="hideSmall">38</td>
<td> 
        +5

 </td>
<td class="points">34</td>
<td class="form hideMed">
<ul>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12050" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Tuesday 8 March 2016</span>
<span class="teamName">ARS</span>
<span class="badge-20 t7606"></span>
<span class="score">1 <span>-</span>2</span>
<span class="badge-20 t7143"></span>
<span class="teamName">MID</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12054" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 12 March 2016</span>
<span class="teamName">MID</span>
<span class="badge-20 t7143"></span>
<span class="score">4 <span>-</span>1</span>
<span class="badge-20 t8879"></span>
<span class="teamName">LEI</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12080" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 9 April 2016</span>
<span class="teamName">MID</span>
<span class="badge-20 t7143"></span>
<span class="score">1 <span>-</span>0</span>
<span class="badge-20 t7631"></span>
<span class="teamName">TOT</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12091" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 16 April 2016</span>
<span class="teamName">WOL</span>
<span class="badge-20 t6746"></span>
<span class="score">2 <span>-</span>3</span>
<span class="badge-20 t7143"></span>
<span class="teamName">MID</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12107" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 30 April 2016</span>
<span class="teamName">MID</span>
<span class="badge-20 t7143"></span>
<span class="score">1 <span>-</span>0</span>
<span class="badge-20 t6753"></span>
<span class="teamName">WBA</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
</ul>
<td class="nextMatchCol hideMed">
</td>
</td>
</tr>
<tr class="expandable" data-filtered-table-row-expander="319">
<td colspan="13">
<a class="expandableTeam" href="/clubs/13/Middlesbrough/overview">
<span class="badge-50 t7143"></span>
<span class="teamName">Middlesbrough</span>
</a>
<div class="expandableFixtures">
<div class="resultWidget">
<div class="label"><strong>Recent Result</strong> - Tuesday 8 March 2016</div>
<a class="matchAbridged pre" href="/match/12107">
<span class="teamName">MID</span>
<span class="badge-20 t7143"></span>
<span class="score">1 <span>-</span>0</span>
<span class="badge-20 t6753"></span>
<span class="teamName">WBA</span>
<span class="icn arrow-right"></span>
</a>
</div>
<div class="btnContainer">
<a class="btn-highlight" href="/clubs/13/Middlesbrough/overview" role="btn">Visit <span class="visuallyHidden">Middlesbrough </span>Club Page<span class="icn arrow-right-w"></span></a>
</div>
</div>
<div class="teamPerformanceStandingsArea" style="display:none;">
<header>
<h3 class="subHeader left">Performance Chart</h3>
<a class="btn right" href="/stats/comparison">Compare against another team<span class="icn arrow-right"></span></a>
</header>
<div class="teamPerformanceStandingsContainer"></div>
</div>
</td>
</tr>
<tr class="" data-compseason="35" data-filtered-entry-size="12" data-filtered-table-row="330" data-filtered-table-row-abbr="330" data-filtered-table-row-name="Wolves" data-filtered-table-row-opta="t6746">
<td class="pos" tabindex="0">
<span class="value">7</span>
</td>
<td class="team" scope="row">
<a href="/clubs/38/Wolverhampton-Wanderers/overview"><span alt="" class="badge-25 t6746"></span><span class="long">Wolverhampton Wanderers</span><span class="short">WOL</span></a>
</td>
<td>22</td>
<td>8</td>
<td>4</td>
<td>10</td>
<td class="hideSmall">42</td>
<td class="hideSmall">40</td>
<td> 
        +2

 </td>
<td class="points">28</td>
<td class="form hideMed">
<ul>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12060" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 12 March 2016</span>
<span class="teamName">WOL</span>
<span class="badge-20 t6746"></span>
<span class="score">1 <span>-</span>2</span>
<span class="badge-20 t7605"></span>
<span class="teamName">AVL</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12067" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 19 March 2016</span>
<span class="teamName">TOT</span>
<span class="badge-20 t7631"></span>
<span class="score">7 <span>-</span>3</span>
<span class="badge-20 t6746"></span>
<span class="teamName">WOL</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12073" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 9 April 2016</span>
<span class="teamName">ARS</span>
<span class="badge-20 t7606"></span>
<span class="score">2 <span>-</span>1</span>
<span class="badge-20 t6746"></span>
<span class="teamName">WOL</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12091" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 16 April 2016</span>
<span class="teamName">WOL</span>
<span class="badge-20 t6746"></span>
<span class="score">2 <span>-</span>3</span>
<span class="badge-20 t7143"></span>
<span class="teamName">MID</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12109" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 30 April 2016</span>
<span class="teamName">SUN</span>
<span class="badge-20 t6756"></span>
<span class="score">4 <span>-</span>1</span>
<span class="badge-20 t6746"></span>
<span class="teamName">WOL</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
</ul>
<td class="nextMatchCol hideMed">
</td>
</td>
</tr>
<tr class="expandable" data-filtered-table-row-expander="330">
<td colspan="13">
<a class="expandableTeam" href="/clubs/38/Wolverhampton-Wanderers/overview">
<span class="badge-50 t6746"></span>
<span class="teamName">Wolverhampton Wanderers</span>
</a>
<div class="expandableFixtures">
<div class="resultWidget">
<div class="label"><strong>Recent Result</strong> - Saturday 12 March 2016</div>
<a class="matchAbridged pre" href="/match/12109">
<span class="teamName">SUN</span>
<span class="badge-20 t6756"></span>
<span class="score">4 <span>-</span>1</span>
<span class="badge-20 t6746"></span>
<span class="teamName">WOL</span>
<span class="icn arrow-right"></span>
</a>
</div>
<div class="btnContainer">
<a class="btn-highlight" href="/clubs/38/Wolverhampton-Wanderers/overview" role="btn">Visit <span class="visuallyHidden">Wolverhampton Wanderers </span>Club Page<span class="icn arrow-right-w"></span></a>
</div>
</div>
<div class="teamPerformanceStandingsArea" style="display:none;">
<header>
<h3 class="subHeader left">Performance Chart</h3>
<a class="btn right" href="/stats/comparison">Compare against another team<span class="icn arrow-right"></span></a>
</header>
<div class="teamPerformanceStandingsContainer"></div>
</div>
</td>
</tr>
<tr class="" data-compseason="35" data-filtered-entry-size="12" data-filtered-table-row="328" data-filtered-table-row-abbr="328" data-filtered-table-row-name="West Brom" data-filtered-table-row-opta="t6753">
<td class="pos" tabindex="0">
<span class="value">8</span>
</td>
<td class="team" scope="row">
<a href="/clubs/36/West-Bromwich-Albion/overview"><span alt="" class="badge-25 t6753"></span><span class="long">West Bromwich Albion</span><span class="short">WBA</span></a>
</td>
<td>22</td>
<td>7</td>
<td>4</td>
<td>11</td>
<td class="hideSmall">29</td>
<td class="hideSmall">44</td>
<td> 
        -15

 </td>
<td class="points">25</td>
<td class="form hideMed">
<ul>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12059" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 12 March 2016</span>
<span class="teamName">WBA</span>
<span class="badge-20 t6753"></span>
<span class="score">2 <span>-</span>1</span>
<span class="badge-20 t7606"></span>
<span class="teamName">ARS</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="draw button-tooltip" id="Tooltip" role="tooltip" tabindex="0">D
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12064" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 19 March 2016</span>
<span class="teamName">LEI</span>
<span class="badge-20 t8879"></span>
<span class="score">1 <span>-</span>1</span>
<span class="badge-20 t6753"></span>
<span class="teamName">WBA</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12074" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 9 April 2016</span>
<span class="teamName">AVL</span>
<span class="badge-20 t7605"></span>
<span class="score">2 <span>-</span>1</span>
<span class="badge-20 t6753"></span>
<span class="teamName">WBA</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12089" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 16 April 2016</span>
<span class="teamName">WBA</span>
<span class="badge-20 t6753"></span>
<span class="score">1 <span>-</span>4</span>
<span class="badge-20 t6756"></span>
<span class="teamName">SUN</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12107" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 30 April 2016</span>
<span class="teamName">MID</span>
<span class="badge-20 t7143"></span>
<span class="score">1 <span>-</span>0</span>
<span class="badge-20 t6753"></span>
<span class="teamName">WBA</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
</ul>
<td class="nextMatchCol hideMed">
</td>
</td>
</tr>
<tr class="expandable" data-filtered-table-row-expander="328">
<td colspan="13">
<a class="expandableTeam" href="/clubs/36/West-Bromwich-Albion/overview">
<span class="badge-50 t6753"></span>
<span class="teamName">West Bromwich Albion</span>
</a>
<div class="expandableFixtures">
<div class="resultWidget">
<div class="label"><strong>Recent Result</strong> - Saturday 12 March 2016</div>
<a class="matchAbridged pre" href="/match/12107">
<span class="teamName">MID</span>
<span class="badge-20 t7143"></span>
<span class="score">1 <span>-</span>0</span>
<span class="badge-20 t6753"></span>
<span class="teamName">WBA</span>
<span class="icn arrow-right"></span>
</a>
</div>
<div class="btnContainer">
<a class="btn-highlight" href="/clubs/36/West-Bromwich-Albion/overview" role="btn">Visit <span class="visuallyHidden">West Bromwich Albion </span>Club Page<span class="icn arrow-right-w"></span></a>
</div>
</div>
<div class="teamPerformanceStandingsArea" style="display:none;">
<header>
<h3 class="subHeader left">Performance Chart</h3>
<a class="btn right" href="/stats/comparison">Compare against another team<span class="icn arrow-right"></span></a>
</header>
<div class="teamPerformanceStandingsContainer"></div>
</div>
</td>
</tr>
<tr class="" data-compseason="35" data-filtered-entry-size="12" data-filtered-table-row="320" data-filtered-table-row-abbr="320" data-filtered-table-row-name="Newcastle United" data-filtered-table-row-opta="t7603">
<td class="pos" tabindex="0">
<span class="value">9</span>
</td>
<td class="team" scope="row">
<a href="/clubs/23/Newcastle-United/overview"><span alt="" class="badge-25 t7603"></span><span class="long">Newcastle United</span><span class="short">NEW</span></a>
</td>
<td>22</td>
<td>6</td>
<td>2</td>
<td>14</td>
<td class="hideSmall">27</td>
<td class="hideSmall">59</td>
<td> 
        -32

 </td>
<td class="points">20</td>
<td class="form hideMed">
<ul>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12057" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 12 March 2016</span>
<span class="teamName">STK</span>
<span class="badge-20 t6747"></span>
<span class="score">2 <span>-</span>1</span>
<span class="badge-20 t7603"></span>
<span class="teamName">NEW</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12071" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 2 April 2016</span>
<span class="teamName">NEW</span>
<span class="badge-20 t7603"></span>
<span class="score">2 <span>-</span>1</span>
<span class="badge-20 t7552"></span>
<span class="teamName">BHA</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12079" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 9 April 2016</span>
<span class="teamName">MUN</span>
<span class="badge-20 t6752"></span>
<span class="score">7 <span>-</span>1</span>
<span class="badge-20 t7603"></span>
<span class="teamName">NEW</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12110" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 30 April 2016</span>
<span class="teamName">SWA</span>
<span class="badge-20 t8967"></span>
<span class="score">2 <span>-</span>1</span>
<span class="badge-20 t7603"></span>
<span class="teamName">NEW</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12114" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 7 May 2016</span>
<span class="teamName">NEW</span>
<span class="badge-20 t7603"></span>
<span class="score">4 <span>-</span>1</span>
<span class="badge-20 t7588"></span>
<span class="teamName">SOU</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
</ul>
<td class="nextMatchCol hideMed">
</td>
</td>
</tr>
<tr class="expandable" data-filtered-table-row-expander="320">
<td colspan="13">
<a class="expandableTeam" href="/clubs/23/Newcastle-United/overview">
<span class="badge-50 t7603"></span>
<span class="teamName">Newcastle United</span>
</a>
<div class="expandableFixtures">
<div class="resultWidget">
<div class="label"><strong>Recent Result</strong> - Saturday 12 March 2016</div>
<a class="matchAbridged pre" href="/match/12114">
<span class="teamName">NEW</span>
<span class="badge-20 t7603"></span>
<span class="score">4 <span>-</span>1</span>
<span class="badge-20 t7588"></span>
<span class="teamName">SOU</span>
<span class="icn arrow-right"></span>
</a>
</div>
<div class="btnContainer">
<a class="btn-highlight" href="/clubs/23/Newcastle-United/overview" role="btn">Visit <span class="visuallyHidden">Newcastle United </span>Club Page<span class="icn arrow-right-w"></span></a>
</div>
</div>
<div class="teamPerformanceStandingsArea" style="display:none;">
<header>
<h3 class="subHeader left">Performance Chart</h3>
<a class="btn right" href="/stats/comparison">Compare against another team<span class="icn arrow-right"></span></a>
</header>
<div class="teamPerformanceStandingsContainer"></div>
</div>
</td>
</tr>
<tr class="" data-compseason="35" data-filtered-entry-size="12" data-filtered-table-row="312" data-filtered-table-row-abbr="312" data-filtered-table-row-name="Derby" data-filtered-table-row-opta="t6757">
<td class="pos" tabindex="0">
<span class="value">10</span>
</td>
<td class="team" scope="row">
<a href="/clubs/28/Derby-County/overview"><span alt="" class="badge-25 t6757"></span><span class="long">Derby County</span><span class="short">DER</span></a>
</td>
<td>22</td>
<td>3</td>
<td>9</td>
<td>10</td>
<td class="hideSmall">39</td>
<td class="hideSmall">51</td>
<td> 
        -12

 </td>
<td class="points">18</td>
<td class="form hideMed">
<ul>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12063" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 19 March 2016</span>
<span class="teamName">DER</span>
<span class="badge-20 t6757"></span>
<span class="score">3 <span>-</span>0</span>
<span class="badge-20 t6752"></span>
<span class="teamName">MUN</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12075" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 9 April 2016</span>
<span class="teamName">BHA</span>
<span class="badge-20 t7552"></span>
<span class="score">2 <span>-</span>1</span>
<span class="badge-20 t6757"></span>
<span class="teamName">DER</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12084" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 16 April 2016</span>
<span class="teamName">DER</span>
<span class="badge-20 t6757"></span>
<span class="score">3 <span>-</span>4</span>
<span class="badge-20 t8967"></span>
<span class="teamName">SWA</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12093" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Friday 22 April 2016</span>
<span class="teamName">SOU</span>
<span class="badge-20 t7588"></span>
<span class="score">0 <span>-</span>1</span>
<span class="badge-20 t6757"></span>
<span class="teamName">DER</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12103" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 30 April 2016</span>
<span class="teamName">DER</span>
<span class="badge-20 t6757"></span>
<span class="score">2 <span>-</span>1</span>
<span class="badge-20 t7604"></span>
<span class="teamName">NOR</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
</ul>
<td class="nextMatchCol hideMed">
</td>
</td>
</tr>
<tr class="expandable" data-filtered-table-row-expander="312">
<td colspan="13">
<a class="expandableTeam" href="/clubs/28/Derby-County/overview">
<span class="badge-50 t6757"></span>
<span class="teamName">Derby County</span>
</a>
<div class="expandableFixtures">
<div class="resultWidget">
<div class="label"><strong>Recent Result</strong> - Saturday 19 March 2016</div>
<a class="matchAbridged pre" href="/match/12103">
<span class="teamName">DER</span>
<span class="badge-20 t6757"></span>
<span class="score">2 <span>-</span>1</span>
<span class="badge-20 t7604"></span>
<span class="teamName">NOR</span>
<span class="icn arrow-right"></span>
</a>
</div>
<div class="btnContainer">
<a class="btn-highlight" href="/clubs/28/Derby-County/overview" role="btn">Visit <span class="visuallyHidden">Derby County </span>Club Page<span class="icn arrow-right-w"></span></a>
</div>
</div>
<div class="teamPerformanceStandingsArea" style="display:none;">
<header>
<h3 class="subHeader left">Performance Chart</h3>
<a class="btn right" href="/stats/comparison">Compare against another team<span class="icn arrow-right"></span></a>
</header>
<div class="teamPerformanceStandingsContainer"></div>
</div>
</td>
</tr>
<tr class="" data-compseason="35" data-filtered-entry-size="12" data-filtered-table-row="318" data-filtered-table-row-abbr="318" data-filtered-table-row-name="Manchester United" data-filtered-table-row-opta="t6752">
<td class="pos" tabindex="0">
<span class="value">11</span>
</td>
<td class="team" scope="row">
<a href="/clubs/12/Manchester-United/overview"><span alt="" class="badge-25 t6752"></span><span class="long">Manchester United</span><span class="short">MUN</span></a>
</td>
<td>22</td>
<td>5</td>
<td>3</td>
<td>14</td>
<td class="hideSmall">29</td>
<td class="hideSmall">44</td>
<td> 
        -15

 </td>
<td class="points">18</td>
<td class="form hideMed">
<ul>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12051" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Friday 11 March 2016</span>
<span class="teamName">MUN</span>
<span class="badge-20 t6752"></span>
<span class="score">1 <span>-</span>2</span>
<span class="badge-20 t7552"></span>
<span class="teamName">BHA</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12063" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 19 March 2016</span>
<span class="teamName">DER</span>
<span class="badge-20 t6757"></span>
<span class="score">3 <span>-</span>0</span>
<span class="badge-20 t6752"></span>
<span class="teamName">MUN</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12079" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 9 April 2016</span>
<span class="teamName">MUN</span>
<span class="badge-20 t6752"></span>
<span class="score">7 <span>-</span>1</span>
<span class="badge-20 t7603"></span>
<span class="teamName">NEW</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12092" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Friday 22 April 2016</span>
<span class="teamName">NOR</span>
<span class="badge-20 t7604"></span>
<span class="score">2 <span>-</span>3</span>
<span class="badge-20 t6752"></span>
<span class="teamName">MUN</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12106" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 30 April 2016</span>
<span class="teamName">MUN</span>
<span class="badge-20 t6752"></span>
<span class="score">1 <span>-</span>0</span>
<span class="badge-20 t7588"></span>
<span class="teamName">SOU</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
</ul>
<td class="nextMatchCol hideMed">
</td>
</td>
</tr>
<tr class="expandable" data-filtered-table-row-expander="318">
<td colspan="13">
<a class="expandableTeam" href="/clubs/12/Manchester-United/overview">
<span class="badge-50 t6752"></span>
<span class="teamName">Manchester United</span>
</a>
<div class="expandableFixtures">
<div class="resultWidget">
<div class="label"><strong>Recent Result</strong> - Friday 11 March 2016</div>
<a class="matchAbridged pre" href="/match/12106">
<span class="teamName">MUN</span>
<span class="badge-20 t6752"></span>
<span class="score">1 <span>-</span>0</span>
<span class="badge-20 t7588"></span>
<span class="teamName">SOU</span>
<span class="icn arrow-right"></span>
</a>
</div>
<div class="btnContainer">
<a class="btn-highlight" href="/clubs/12/Manchester-United/overview" role="btn">Visit <span class="visuallyHidden">Manchester United </span>Club Page<span class="icn arrow-right-w"></span></a>
</div>
</div>
<div class="teamPerformanceStandingsArea" style="display:none;">
<header>
<h3 class="subHeader left">Performance Chart</h3>
<a class="btn right" href="/stats/comparison">Compare against another team<span class="icn arrow-right"></span></a>
</header>
<div class="teamPerformanceStandingsContainer"></div>
</div>
</td>
</tr>
<tr class="" data-compseason="35" data-filtered-entry-size="12" data-filtered-table-row="324" data-filtered-table-row-abbr="324" data-filtered-table-row-name="Stoke" data-filtered-table-row-opta="t6747">
<td class="pos" tabindex="0">
<span class="value">12</span>
</td>
<td class="team" scope="row">
<a href="/clubs/42/Stoke-City/overview"><span alt="" class="badge-25 t6747"></span><span class="long">Stoke City</span><span class="short">STK</span></a>
</td>
<td>22</td>
<td>4</td>
<td>4</td>
<td>14</td>
<td class="hideSmall">23</td>
<td class="hideSmall">45</td>
<td> 
        -22

 </td>
<td class="points">16</td>
<td class="form hideMed">
<ul>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12057" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 12 March 2016</span>
<span class="teamName">STK</span>
<span class="badge-20 t6747"></span>
<span class="score">2 <span>-</span>1</span>
<span class="badge-20 t7603"></span>
<span class="teamName">NEW</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12066" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 19 March 2016</span>
<span class="teamName">NOR</span>
<span class="badge-20 t7604"></span>
<span class="score">2 <span>-</span>3</span>
<span class="badge-20 t6747"></span>
<span class="teamName">STK</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12082" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 9 April 2016</span>
<span class="teamName">SWA</span>
<span class="badge-20 t8967"></span>
<span class="score">2 <span>-</span>1</span>
<span class="badge-20 t6747"></span>
<span class="teamName">STK</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12087" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 16 April 2016</span>
<span class="teamName">STK</span>
<span class="badge-20 t6747"></span>
<span class="score">1 <span>-</span>0</span>
<span class="badge-20 t7588"></span>
<span class="teamName">SOU</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12102" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 30 April 2016</span>
<span class="teamName">BHA</span>
<span class="badge-20 t7552"></span>
<span class="score">2 <span>-</span>1</span>
<span class="badge-20 t6747"></span>
<span class="teamName">STK</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
</ul>
<td class="nextMatchCol hideMed">
</td>
</td>
</tr>
<tr class="expandable" data-filtered-table-row-expander="324">
<td colspan="13">
<a class="expandableTeam" href="/clubs/42/Stoke-City/overview">
<span class="badge-50 t6747"></span>
<span class="teamName">Stoke City</span>
</a>
<div class="expandableFixtures">
<div class="resultWidget">
<div class="label"><strong>Recent Result</strong> - Saturday 12 March 2016</div>
<a class="matchAbridged pre" href="/match/12102">
<span class="teamName">BHA</span>
<span class="badge-20 t7552"></span>
<span class="score">2 <span>-</span>1</span>
<span class="badge-20 t6747"></span>
<span class="teamName">STK</span>
<span class="icn arrow-right"></span>
</a>
</div>
<div class="btnContainer">
<a class="btn-highlight" href="/clubs/42/Stoke-City/overview" role="btn">Visit <span class="visuallyHidden">Stoke City </span>Club Page<span class="icn arrow-right-w"></span></a>
</div>
</div>
<div class="teamPerformanceStandingsArea" style="display:none;">
<header>
<h3 class="subHeader left">Performance Chart</h3>
<a class="btn right" href="/stats/comparison">Compare against another team<span class="icn arrow-right"></span></a>
</header>
<div class="teamPerformanceStandingsContainer"></div>
</div>
</td>
</tr>
</tbody>
</table>
</div>, <div class="table wrapper col-12">
<table>
<summary class="visuallyHidden">This table charts the Premier League teams</summary>
<thead>
<tr>
<th class="text-centre" scope="col">
<div class="thFull">Position</div>
<div class="thShort">Pos</div>
</th>
<th class="team" scope="col">Club</th>
<th scope="col">
<div class="thFull">Played</div>
<div class="thShort">Pl</div>
</th>
<th scope="col">
<div class="thFull">Won</div>
<div class="thShort">W</div>
</th>
<th scope="col">
<div class="thFull">Drawn</div>
<div class="thShort">D</div>
</th>
<th scope="col">
<div class="thFull">Lost</div>
<div class="thShort">L</div>
</th>
<th class="hideSmall" scope="col"><abbr title="Goals For">GF</abbr></th>
<th class="hideSmall" scope="col"><abbr title="Goals Against">GA</abbr></th>
<th scope="col"><abbr title="Goal Difference">GD</abbr></th>
<th class="points" scope="col">
<div class="thFull">Points</div>
<div class="thShort">Pts</div>
</th>
<th class="teamForm hideMed" scope="col">Form</th>
<th class="hideMed text-centre" scope="col">Next</th>
</tr>
</thead>
<tbody class="tableBodyContainer">
<tr class="tableDark" data-compseason="35" data-filtered-entry-size="12" data-filtered-table-row="311" data-filtered-table-row-abbr="311" data-filtered-table-row-name="Chelsea" data-filtered-table-row-opta="t7141">
<td class="pos" tabindex="0">
<span class="value">1</span>
</td>
<td class="team" scope="row">
<a href="/clubs/4/Chelsea/overview"><span alt="" class="badge-25 t7141"></span><span class="long">Chelsea</span><span class="short">CHE</span></a>
</td>
<td>22</td>
<td>15</td>
<td>5</td>
<td>2</td>
<td class="hideSmall">65</td>
<td class="hideSmall">27</td>
<td> 
        +38

 </td>
<td class="points">50</td>
<td class="form hideMed">
<ul>
<li class="draw button-tooltip" id="Tooltip" role="tooltip" tabindex="0">D
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12062" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 19 March 2016</span>
<span class="teamName">CHE</span>
<span class="badge-20 t7141"></span>
<span class="score">2 <span>-</span>2</span>
<span class="badge-20 t7632"></span>
<span class="teamName">WHU</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12068" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 2 April 2016</span>
<span class="teamName">CHE</span>
<span class="badge-20 t7141"></span>
<span class="score">6 <span>-</span>2</span>
<span class="badge-20 t7587"></span>
<span class="teamName">RDG</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12077" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 9 April 2016</span>
<span class="teamName">FUL</span>
<span class="badge-20 t6886"></span>
<span class="score">0 <span>-</span>2</span>
<span class="badge-20 t7141"></span>
<span class="teamName">CHE</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="draw button-tooltip" id="Tooltip" role="tooltip" tabindex="0">D
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12099" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Friday 29 April 2016</span>
<span class="teamName">CHE</span>
<span class="badge-20 t7141"></span>
<span class="score">2 <span>-</span>2</span>
<span class="badge-20 t6717"></span>
<span class="teamName">LIV</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12112" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 7 May 2016</span>
<span class="teamName">BLB</span>
<span class="badge-20 t6748"></span>
<span class="score">3 <span>-</span>0</span>
<span class="badge-20 t7141"></span>
<span class="teamName">CHE</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
</ul>
<td class="nextMatchCol hideMed">
</td>
</td>
</tr>
<tr class="expandable" data-filtered-table-row-expander="311">
<td colspan="13">
<a class="expandableTeam" href="/clubs/4/Chelsea/overview">
<span class="badge-50 t7141"></span>
<span class="teamName">Chelsea</span>
</a>
<div class="expandableFixtures">
<div class="resultWidget">
<div class="label"><strong>Recent Result</strong> - Saturday 19 March 2016</div>
<a class="matchAbridged pre" href="/match/12112">
<span class="teamName">BLB</span>
<span class="badge-20 t6748"></span>
<span class="score">3 <span>-</span>0</span>
<span class="badge-20 t7141"></span>
<span class="teamName">CHE</span>
<span class="icn arrow-right"></span>
</a>
</div>
<div class="btnContainer">
<a class="btn-highlight" href="/clubs/4/Chelsea/overview" role="btn">Visit <span class="visuallyHidden">Chelsea </span>Club Page<span class="icn arrow-right-w"></span></a>
</div>
</div>
<div class="teamPerformanceStandingsArea" style="display:none;">
<header>
<h3 class="subHeader left">Performance Chart</h3>
<a class="btn right" href="/stats/comparison">Compare against another team<span class="icn arrow-right"></span></a>
</header>
<div class="teamPerformanceStandingsContainer"></div>
</div>
</td>
</tr>
<tr class="" data-compseason="35" data-filtered-entry-size="12" data-filtered-table-row="322" data-filtered-table-row-abbr="322" data-filtered-table-row-name="Reading" data-filtered-table-row-opta="t7587">
<td class="pos" tabindex="0">
<span class="value">2</span>
</td>
<td class="team" scope="row">
<a href="/clubs/40/Reading/overview"><span alt="" class="badge-25 t7587"></span><span class="long">Reading</span><span class="short">RDG</span></a>
</td>
<td>22</td>
<td>13</td>
<td>3</td>
<td>6</td>
<td class="hideSmall">47</td>
<td class="hideSmall">27</td>
<td> 
        +20

 </td>
<td class="points">42</td>
<td class="form hideMed">
<ul>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12065" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 19 March 2016</span>
<span class="teamName">LIV</span>
<span class="badge-20 t6717"></span>
<span class="score">1 <span>-</span>4</span>
<span class="badge-20 t7587"></span>
<span class="teamName">RDG</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12068" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 2 April 2016</span>
<span class="teamName">CHE</span>
<span class="badge-20 t7141"></span>
<span class="score">6 <span>-</span>2</span>
<span class="badge-20 t7587"></span>
<span class="teamName">RDG</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="draw button-tooltip" id="Tooltip" role="tooltip" tabindex="0">D
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12090" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 16 April 2016</span>
<span class="teamName">WHU</span>
<span class="badge-20 t7632"></span>
<span class="score">1 <span>-</span>1</span>
<span class="badge-20 t7587"></span>
<span class="teamName">RDG</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="draw button-tooltip" id="Tooltip" role="tooltip" tabindex="0">D
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12095" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 23 April 2016</span>
<span class="teamName">RDG</span>
<span class="badge-20 t7587"></span>
<span class="score">1 <span>-</span>1</span>
<span class="badge-20 t6748"></span>
<span class="teamName">BLB</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12108" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 30 April 2016</span>
<span class="teamName">RDG</span>
<span class="badge-20 t7587"></span>
<span class="score">1 <span>-</span>2</span>
<span class="badge-20 t6886"></span>
<span class="teamName">FUL</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
</ul>
<td class="nextMatchCol hideMed">
</td>
</td>
</tr>
<tr class="expandable" data-filtered-table-row-expander="322">
<td colspan="13">
<a class="expandableTeam" href="/clubs/40/Reading/overview">
<span class="badge-50 t7587"></span>
<span class="teamName">Reading</span>
</a>
<div class="expandableFixtures">
<div class="resultWidget">
<div class="label"><strong>Recent Result</strong> - Saturday 19 March 2016</div>
<a class="matchAbridged pre" href="/match/12108">
<span class="teamName">RDG</span>
<span class="badge-20 t7587"></span>
<span class="score">1 <span>-</span>2</span>
<span class="badge-20 t6886"></span>
<span class="teamName">FUL</span>
<span class="icn arrow-right"></span>
</a>
</div>
<div class="btnContainer">
<a class="btn-highlight" href="/clubs/40/Reading/overview" role="btn">Visit <span class="visuallyHidden">Reading </span>Club Page<span class="icn arrow-right-w"></span></a>
</div>
</div>
<div class="teamPerformanceStandingsArea" style="display:none;">
<header>
<h3 class="subHeader left">Performance Chart</h3>
<a class="btn right" href="/stats/comparison">Compare against another team<span class="icn arrow-right"></span></a>
</header>
<div class="teamPerformanceStandingsContainer"></div>
</div>
</td>
</tr>
<tr class="" data-compseason="35" data-filtered-entry-size="12" data-filtered-table-row="314" data-filtered-table-row-abbr="314" data-filtered-table-row-name="Fulham" data-filtered-table-row-opta="t6886">
<td class="pos" tabindex="0">
<span class="value">3</span>
</td>
<td class="team" scope="row">
<a href="/clubs/34/Fulham/overview"><span alt="" class="badge-25 t6886"></span><span class="long">Fulham</span><span class="short">FUL</span></a>
</td>
<td>22</td>
<td>12</td>
<td>3</td>
<td>7</td>
<td class="hideSmall">44</td>
<td class="hideSmall">29</td>
<td> 
        +15

 </td>
<td class="points">39</td>
<td class="form hideMed">
<ul>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12070" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 2 April 2016</span>
<span class="teamName">FUL</span>
<span class="badge-20 t6886"></span>
<span class="score">1 <span>-</span>5</span>
<span class="badge-20 t6717"></span>
<span class="teamName">LIV</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12077" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 9 April 2016</span>
<span class="teamName">FUL</span>
<span class="badge-20 t6886"></span>
<span class="score">0 <span>-</span>2</span>
<span class="badge-20 t7141"></span>
<span class="teamName">CHE</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12085" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 16 April 2016</span>
<span class="teamName">FUL</span>
<span class="badge-20 t6886"></span>
<span class="score">2 <span>-</span>3</span>
<span class="badge-20 t6749"></span>
<span class="teamName">EVE</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12108" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 30 April 2016</span>
<span class="teamName">RDG</span>
<span class="badge-20 t7587"></span>
<span class="score">1 <span>-</span>2</span>
<span class="badge-20 t6886"></span>
<span class="teamName">FUL</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12113" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 7 May 2016</span>
<span class="teamName">MCI</span>
<span class="badge-20 t6718"></span>
<span class="score">5 <span>-</span>0</span>
<span class="badge-20 t6886"></span>
<span class="teamName">FUL</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
</ul>
<td class="nextMatchCol hideMed">
</td>
</td>
</tr>
<tr class="expandable" data-filtered-table-row-expander="314">
<td colspan="13">
<a class="expandableTeam" href="/clubs/34/Fulham/overview">
<span class="badge-50 t6886"></span>
<span class="teamName">Fulham</span>
</a>
<div class="expandableFixtures">
<div class="resultWidget">
<div class="label"><strong>Recent Result</strong> - Saturday 2 April 2016</div>
<a class="matchAbridged pre" href="/match/12113">
<span class="teamName">MCI</span>
<span class="badge-20 t6718"></span>
<span class="score">5 <span>-</span>0</span>
<span class="badge-20 t6886"></span>
<span class="teamName">FUL</span>
<span class="icn arrow-right"></span>
</a>
</div>
<div class="btnContainer">
<a class="btn-highlight" href="/clubs/34/Fulham/overview" role="btn">Visit <span class="visuallyHidden">Fulham </span>Club Page<span class="icn arrow-right-w"></span></a>
</div>
</div>
<div class="teamPerformanceStandingsArea" style="display:none;">
<header>
<h3 class="subHeader left">Performance Chart</h3>
<a class="btn right" href="/stats/comparison">Compare against another team<span class="icn arrow-right"></span></a>
</header>
<div class="teamPerformanceStandingsContainer"></div>
</div>
</td>
</tr>
<tr class="" data-compseason="35" data-filtered-entry-size="12" data-filtered-table-row="329" data-filtered-table-row-abbr="329" data-filtered-table-row-name="West Ham United" data-filtered-table-row-opta="t7632">
<td class="pos" tabindex="0">
<span class="value">4</span>
</td>
<td class="team" scope="row">
<a href="/clubs/25/West-Ham-United/overview"><span alt="" class="badge-25 t7632"></span><span class="long">West Ham United</span><span class="short">WHU</span></a>
</td>
<td>22</td>
<td>11</td>
<td>4</td>
<td>7</td>
<td class="hideSmall">30</td>
<td class="hideSmall">29</td>
<td> 
        +1

 </td>
<td class="points">37</td>
<td class="form hideMed">
<ul>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12078" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 9 April 2016</span>
<span class="teamName">MCI</span>
<span class="badge-20 t6718"></span>
<span class="score">3 <span>-</span>0</span>
<span class="badge-20 t7632"></span>
<span class="teamName">WHU</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="draw button-tooltip" id="Tooltip" role="tooltip" tabindex="0">D
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12090" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 16 April 2016</span>
<span class="teamName">WHU</span>
<span class="badge-20 t7632"></span>
<span class="score">1 <span>-</span>1</span>
<span class="badge-20 t7587"></span>
<span class="teamName">RDG</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="draw button-tooltip" id="Tooltip" role="tooltip" tabindex="0">D
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12097" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 23 April 2016</span>
<span class="teamName">WHU</span>
<span class="badge-20 t7632"></span>
<span class="score">0 <span>-</span>0</span>
<span class="badge-20 t6717"></span>
<span class="teamName">LIV</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="draw button-tooltip" id="Tooltip" role="tooltip" tabindex="0">D
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12098" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Wednesday 27 April 2016</span>
<span class="teamName">BLB</span>
<span class="badge-20 t6748"></span>
<span class="score">1 <span>-</span>1</span>
<span class="badge-20 t7632"></span>
<span class="teamName">WHU</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12104" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 30 April 2016</span>
<span class="teamName">EVE</span>
<span class="badge-20 t6749"></span>
<span class="score">4 <span>-</span>3</span>
<span class="badge-20 t7632"></span>
<span class="teamName">WHU</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
</ul>
<td class="nextMatchCol hideMed">
</td>
</td>
</tr>
<tr class="expandable" data-filtered-table-row-expander="329">
<td colspan="13">
<a class="expandableTeam" href="/clubs/25/West-Ham-United/overview">
<span class="badge-50 t7632"></span>
<span class="teamName">West Ham United</span>
</a>
<div class="expandableFixtures">
<div class="resultWidget">
<div class="label"><strong>Recent Result</strong> - Saturday 9 April 2016</div>
<a class="matchAbridged pre" href="/match/12104">
<span class="teamName">EVE</span>
<span class="badge-20 t6749"></span>
<span class="score">4 <span>-</span>3</span>
<span class="badge-20 t7632"></span>
<span class="teamName">WHU</span>
<span class="icn arrow-right"></span>
</a>
</div>
<div class="btnContainer">
<a class="btn-highlight" href="/clubs/25/West-Ham-United/overview" role="btn">Visit <span class="visuallyHidden">West Ham United </span>Club Page<span class="icn arrow-right-w"></span></a>
</div>
</div>
<div class="teamPerformanceStandingsArea" style="display:none;">
<header>
<h3 class="subHeader left">Performance Chart</h3>
<a class="btn right" href="/stats/comparison">Compare against another team<span class="icn arrow-right"></span></a>
</header>
<div class="teamPerformanceStandingsContainer"></div>
</div>
</td>
</tr>
<tr class="" data-compseason="35" data-filtered-entry-size="12" data-filtered-table-row="308" data-filtered-table-row-abbr="308" data-filtered-table-row-name="Aston Villa" data-filtered-table-row-opta="t7605">
<td class="pos" tabindex="0">
<span class="value">5</span>
</td>
<td class="team" scope="row">
<a href="/clubs/2/Aston-Villa/overview"><span alt="" class="badge-25 t7605"></span><span class="long">Aston Villa</span><span class="short">AVL</span></a>
</td>
<td>22</td>
<td>11</td>
<td>3</td>
<td>8</td>
<td class="hideSmall">42</td>
<td class="hideSmall">34</td>
<td> 
        +8

 </td>
<td class="points">36</td>
<td class="form hideMed">
<ul>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12060" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 12 March 2016</span>
<span class="teamName">WOL</span>
<span class="badge-20 t6746"></span>
<span class="score">1 <span>-</span>2</span>
<span class="badge-20 t7605"></span>
<span class="teamName">AVL</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12061" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 19 March 2016</span>
<span class="teamName">AVL</span>
<span class="badge-20 t7605"></span>
<span class="score">0 <span>-</span>1</span>
<span class="badge-20 t6756"></span>
<span class="teamName">SUN</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12074" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 9 April 2016</span>
<span class="teamName">AVL</span>
<span class="badge-20 t7605"></span>
<span class="score">2 <span>-</span>1</span>
<span class="badge-20 t6753"></span>
<span class="teamName">WBA</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12088" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 16 April 2016</span>
<span class="teamName">TOT</span>
<span class="badge-20 t7631"></span>
<span class="score">0 <span>-</span>1</span>
<span class="badge-20 t7605"></span>
<span class="teamName">AVL</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="draw button-tooltip" id="Tooltip" role="tooltip" tabindex="0">D
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12101" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 30 April 2016</span>
<span class="teamName">AVL</span>
<span class="badge-20 t7605"></span>
<span class="score">1 <span>-</span>1</span>
<span class="badge-20 t8879"></span>
<span class="teamName">LEI</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
</ul>
<td class="nextMatchCol hideMed">
</td>
</td>
</tr>
<tr class="expandable" data-filtered-table-row-expander="308">
<td colspan="13">
<a class="expandableTeam" href="/clubs/2/Aston-Villa/overview">
<span class="badge-50 t7605"></span>
<span class="teamName">Aston Villa</span>
</a>
<div class="expandableFixtures">
<div class="resultWidget">
<div class="label"><strong>Recent Result</strong> - Saturday 12 March 2016</div>
<a class="matchAbridged pre" href="/match/12101">
<span class="teamName">AVL</span>
<span class="badge-20 t7605"></span>
<span class="score">1 <span>-</span>1</span>
<span class="badge-20 t8879"></span>
<span class="teamName">LEI</span>
<span class="icn arrow-right"></span>
</a>
</div>
<div class="btnContainer">
<a class="btn-highlight" href="/clubs/2/Aston-Villa/overview" role="btn">Visit <span class="visuallyHidden">Aston Villa </span>Club Page<span class="icn arrow-right-w"></span></a>
</div>
</div>
<div class="teamPerformanceStandingsArea" style="display:none;">
<header>
<h3 class="subHeader left">Performance Chart</h3>
<a class="btn right" href="/stats/comparison">Compare against another team<span class="icn arrow-right"></span></a>
</header>
<div class="teamPerformanceStandingsContainer"></div>
</div>
</td>
</tr>
<tr class="" data-compseason="35" data-filtered-entry-size="12" data-filtered-table-row="307" data-filtered-table-row-abbr="307" data-filtered-table-row-name="Arsenal" data-filtered-table-row-opta="t7606">
<td class="pos" tabindex="0">
<span class="value">6</span>
</td>
<td class="team" scope="row">
<a href="/clubs/1/Arsenal/overview"><span alt="" class="badge-25 t7606"></span><span class="long">Arsenal</span><span class="short">ARS</span></a>
</td>
<td>22</td>
<td>10</td>
<td>5</td>
<td>7</td>
<td class="hideSmall">49</td>
<td class="hideSmall">45</td>
<td> 
        +4

 </td>
<td class="points">35</td>
<td class="form hideMed">
<ul>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12059" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 12 March 2016</span>
<span class="teamName">WBA</span>
<span class="badge-20 t6753"></span>
<span class="score">2 <span>-</span>1</span>
<span class="badge-20 t7606"></span>
<span class="teamName">ARS</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12073" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 9 April 2016</span>
<span class="teamName">ARS</span>
<span class="badge-20 t7606"></span>
<span class="score">2 <span>-</span>1</span>
<span class="badge-20 t6746"></span>
<span class="teamName">WOL</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12083" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 16 April 2016</span>
<span class="teamName">ARS</span>
<span class="badge-20 t7606"></span>
<span class="score">1 <span>-</span>2</span>
<span class="badge-20 t8879"></span>
<span class="teamName">LEI</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12096" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 23 April 2016</span>
<span class="teamName">SUN</span>
<span class="badge-20 t6756"></span>
<span class="score">1 <span>-</span>4</span>
<span class="badge-20 t7606"></span>
<span class="teamName">ARS</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="draw button-tooltip" id="Tooltip" role="tooltip" tabindex="0">D
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12100" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 30 April 2016</span>
<span class="teamName">ARS</span>
<span class="badge-20 t7606"></span>
<span class="score">3 <span>-</span>3</span>
<span class="badge-20 t7631"></span>
<span class="teamName">TOT</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
</ul>
<td class="nextMatchCol hideMed">
</td>
</td>
</tr>
<tr class="expandable" data-filtered-table-row-expander="307">
<td colspan="13">
<a class="expandableTeam" href="/clubs/1/Arsenal/overview">
<span class="badge-50 t7606"></span>
<span class="teamName">Arsenal</span>
</a>
<div class="expandableFixtures">
<div class="resultWidget">
<div class="label"><strong>Recent Result</strong> - Saturday 12 March 2016</div>
<a class="matchAbridged pre" href="/match/12100">
<span class="teamName">ARS</span>
<span class="badge-20 t7606"></span>
<span class="score">3 <span>-</span>3</span>
<span class="badge-20 t7631"></span>
<span class="teamName">TOT</span>
<span class="icn arrow-right"></span>
</a>
</div>
<div class="btnContainer">
<a class="btn-highlight" href="/clubs/1/Arsenal/overview" role="btn">Visit <span class="visuallyHidden">Arsenal </span>Club Page<span class="icn arrow-right-w"></span></a>
</div>
</div>
<div class="teamPerformanceStandingsArea" style="display:none;">
<header>
<h3 class="subHeader left">Performance Chart</h3>
<a class="btn right" href="/stats/comparison">Compare against another team<span class="icn arrow-right"></span></a>
</header>
<div class="teamPerformanceStandingsContainer"></div>
</div>
</td>
</tr>
<tr class="" data-compseason="35" data-filtered-entry-size="12" data-filtered-table-row="315" data-filtered-table-row-abbr="315" data-filtered-table-row-name="Leicester City" data-filtered-table-row-opta="t8879">
<td class="pos" tabindex="0">
<span class="value">7</span>
</td>
<td class="team" scope="row">
<a href="/clubs/26/Leicester-City/overview"><span alt="" class="badge-25 t8879"></span><span class="long">Leicester City</span><span class="short">LEI</span></a>
</td>
<td>22</td>
<td>9</td>
<td>5</td>
<td>8</td>
<td class="hideSmall">39</td>
<td class="hideSmall">37</td>
<td> 
        +2

 </td>
<td class="points">32</td>
<td class="form hideMed">
<ul>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12054" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 12 March 2016</span>
<span class="teamName">MID</span>
<span class="badge-20 t7143"></span>
<span class="score">4 <span>-</span>1</span>
<span class="badge-20 t8879"></span>
<span class="teamName">LEI</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="draw button-tooltip" id="Tooltip" role="tooltip" tabindex="0">D
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12064" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 19 March 2016</span>
<span class="teamName">LEI</span>
<span class="badge-20 t8879"></span>
<span class="score">1 <span>-</span>1</span>
<span class="badge-20 t6753"></span>
<span class="teamName">WBA</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="draw button-tooltip" id="Tooltip" role="tooltip" tabindex="0">D
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12072" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Friday 8 April 2016</span>
<span class="teamName">SUN</span>
<span class="badge-20 t6756"></span>
<span class="score">1 <span>-</span>1</span>
<span class="badge-20 t8879"></span>
<span class="teamName">LEI</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12083" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 16 April 2016</span>
<span class="teamName">ARS</span>
<span class="badge-20 t7606"></span>
<span class="score">1 <span>-</span>2</span>
<span class="badge-20 t8879"></span>
<span class="teamName">LEI</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="draw button-tooltip" id="Tooltip" role="tooltip" tabindex="0">D
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12101" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 30 April 2016</span>
<span class="teamName">AVL</span>
<span class="badge-20 t7605"></span>
<span class="score">1 <span>-</span>1</span>
<span class="badge-20 t8879"></span>
<span class="teamName">LEI</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
</ul>
<td class="nextMatchCol hideMed">
</td>
</td>
</tr>
<tr class="expandable" data-filtered-table-row-expander="315">
<td colspan="13">
<a class="expandableTeam" href="/clubs/26/Leicester-City/overview">
<span class="badge-50 t8879"></span>
<span class="teamName">Leicester City</span>
</a>
<div class="expandableFixtures">
<div class="resultWidget">
<div class="label"><strong>Recent Result</strong> - Saturday 12 March 2016</div>
<a class="matchAbridged pre" href="/match/12101">
<span class="teamName">AVL</span>
<span class="badge-20 t7605"></span>
<span class="score">1 <span>-</span>1</span>
<span class="badge-20 t8879"></span>
<span class="teamName">LEI</span>
<span class="icn arrow-right"></span>
</a>
</div>
<div class="btnContainer">
<a class="btn-highlight" href="/clubs/26/Leicester-City/overview" role="btn">Visit <span class="visuallyHidden">Leicester City </span>Club Page<span class="icn arrow-right-w"></span></a>
</div>
</div>
<div class="teamPerformanceStandingsArea" style="display:none;">
<header>
<h3 class="subHeader left">Performance Chart</h3>
<a class="btn right" href="/stats/comparison">Compare against another team<span class="icn arrow-right"></span></a>
</header>
<div class="teamPerformanceStandingsContainer"></div>
</div>
</td>
</tr>
<tr class="" data-compseason="35" data-filtered-entry-size="12" data-filtered-table-row="327" data-filtered-table-row-abbr="327" data-filtered-table-row-name="Spurs" data-filtered-table-row-opta="t7631">
<td class="pos" tabindex="0">
<span class="value">8</span>
</td>
<td class="team" scope="row">
<a href="/clubs/21/Tottenham-Hotspur/overview"><span alt="" class="badge-25 t7631"></span><span class="long">Tottenham Hotspur</span><span class="short">TOT</span></a>
</td>
<td>22</td>
<td>9</td>
<td>4</td>
<td>9</td>
<td class="hideSmall">43</td>
<td class="hideSmall">40</td>
<td> 
        +3

 </td>
<td class="points">31</td>
<td class="form hideMed">
<ul>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12058" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 12 March 2016</span>
<span class="teamName">SUN</span>
<span class="badge-20 t6756"></span>
<span class="score">3 <span>-</span>0</span>
<span class="badge-20 t7631"></span>
<span class="teamName">TOT</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12067" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 19 March 2016</span>
<span class="teamName">TOT</span>
<span class="badge-20 t7631"></span>
<span class="score">7 <span>-</span>3</span>
<span class="badge-20 t6746"></span>
<span class="teamName">WOL</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12080" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 9 April 2016</span>
<span class="teamName">MID</span>
<span class="badge-20 t7143"></span>
<span class="score">1 <span>-</span>0</span>
<span class="badge-20 t7631"></span>
<span class="teamName">TOT</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12088" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 16 April 2016</span>
<span class="teamName">TOT</span>
<span class="badge-20 t7631"></span>
<span class="score">0 <span>-</span>1</span>
<span class="badge-20 t7605"></span>
<span class="teamName">AVL</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="draw button-tooltip" id="Tooltip" role="tooltip" tabindex="0">D
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12100" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 30 April 2016</span>
<span class="teamName">ARS</span>
<span class="badge-20 t7606"></span>
<span class="score">3 <span>-</span>3</span>
<span class="badge-20 t7631"></span>
<span class="teamName">TOT</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
</ul>
<td class="nextMatchCol hideMed">
</td>
</td>
</tr>
<tr class="expandable" data-filtered-table-row-expander="327">
<td colspan="13">
<a class="expandableTeam" href="/clubs/21/Tottenham-Hotspur/overview">
<span class="badge-50 t7631"></span>
<span class="teamName">Tottenham Hotspur</span>
</a>
<div class="expandableFixtures">
<div class="resultWidget">
<div class="label"><strong>Recent Result</strong> - Saturday 12 March 2016</div>
<a class="matchAbridged pre" href="/match/12100">
<span class="teamName">ARS</span>
<span class="badge-20 t7606"></span>
<span class="score">3 <span>-</span>3</span>
<span class="badge-20 t7631"></span>
<span class="teamName">TOT</span>
<span class="icn arrow-right"></span>
</a>
</div>
<div class="btnContainer">
<a class="btn-highlight" href="/clubs/21/Tottenham-Hotspur/overview" role="btn">Visit <span class="visuallyHidden">Tottenham Hotspur </span>Club Page<span class="icn arrow-right-w"></span></a>
</div>
</div>
<div class="teamPerformanceStandingsArea" style="display:none;">
<header>
<h3 class="subHeader left">Performance Chart</h3>
<a class="btn right" href="/stats/comparison">Compare against another team<span class="icn arrow-right"></span></a>
</header>
<div class="teamPerformanceStandingsContainer"></div>
</div>
</td>
</tr>
<tr class="" data-compseason="35" data-filtered-entry-size="12" data-filtered-table-row="310" data-filtered-table-row-abbr="310" data-filtered-table-row-name="Brighton" data-filtered-table-row-opta="t7552">
<td class="pos" tabindex="0">
<span class="value">9</span>
</td>
<td class="team" scope="row">
<a href="/clubs/131/Brighton-and-Hove-Albion/overview"><span alt="" class="badge-25 t7552"></span><span class="long">Brighton and Hove Albion</span><span class="short">BHA</span></a>
</td>
<td>22</td>
<td>6</td>
<td>4</td>
<td>12</td>
<td class="hideSmall">32</td>
<td class="hideSmall">51</td>
<td> 
        -19

 </td>
<td class="points">22</td>
<td class="form hideMed">
<ul>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12051" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Friday 11 March 2016</span>
<span class="teamName">MUN</span>
<span class="badge-20 t6752"></span>
<span class="score">1 <span>-</span>2</span>
<span class="badge-20 t7552"></span>
<span class="teamName">BHA</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12071" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 2 April 2016</span>
<span class="teamName">NEW</span>
<span class="badge-20 t7603"></span>
<span class="score">2 <span>-</span>1</span>
<span class="badge-20 t7552"></span>
<span class="teamName">BHA</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12075" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 9 April 2016</span>
<span class="teamName">BHA</span>
<span class="badge-20 t7552"></span>
<span class="score">2 <span>-</span>1</span>
<span class="badge-20 t6757"></span>
<span class="teamName">DER</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="draw button-tooltip" id="Tooltip" role="tooltip" tabindex="0">D
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12094" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 23 April 2016</span>
<span class="teamName">BHA</span>
<span class="badge-20 t7552"></span>
<span class="score">3 <span>-</span>3</span>
<span class="badge-20 t8967"></span>
<span class="teamName">SWA</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12102" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 30 April 2016</span>
<span class="teamName">BHA</span>
<span class="badge-20 t7552"></span>
<span class="score">2 <span>-</span>1</span>
<span class="badge-20 t6747"></span>
<span class="teamName">STK</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
</ul>
<td class="nextMatchCol hideMed">
</td>
</td>
</tr>
<tr class="expandable" data-filtered-table-row-expander="310">
<td colspan="13">
<a class="expandableTeam" href="/clubs/131/Brighton-and-Hove-Albion/overview">
<span class="badge-50 t7552"></span>
<span class="teamName">Brighton and Hove Albion</span>
</a>
<div class="expandableFixtures">
<div class="resultWidget">
<div class="label"><strong>Recent Result</strong> - Friday 11 March 2016</div>
<a class="matchAbridged pre" href="/match/12102">
<span class="teamName">BHA</span>
<span class="badge-20 t7552"></span>
<span class="score">2 <span>-</span>1</span>
<span class="badge-20 t6747"></span>
<span class="teamName">STK</span>
<span class="icn arrow-right"></span>
</a>
</div>
<div class="btnContainer">
<a class="btn-highlight" href="/clubs/131/Brighton-and-Hove-Albion/overview" role="btn">Visit <span class="visuallyHidden">Brighton and Hove Albion </span>Club Page<span class="icn arrow-right-w"></span></a>
</div>
</div>
<div class="teamPerformanceStandingsArea" style="display:none;">
<header>
<h3 class="subHeader left">Performance Chart</h3>
<a class="btn right" href="/stats/comparison">Compare against another team<span class="icn arrow-right"></span></a>
</header>
<div class="teamPerformanceStandingsContainer"></div>
</div>
</td>
</tr>
<tr class="" data-compseason="35" data-filtered-entry-size="12" data-filtered-table-row="321" data-filtered-table-row-abbr="321" data-filtered-table-row-name="Norwich" data-filtered-table-row-opta="t7604">
<td class="pos" tabindex="0">
<span class="value">10</span>
</td>
<td class="team" scope="row">
<a href="/clubs/14/Norwich-City/overview"><span alt="" class="badge-25 t7604"></span><span class="long">Norwich City</span><span class="short">NOR</span></a>
</td>
<td>22</td>
<td>6</td>
<td>3</td>
<td>13</td>
<td class="hideSmall">28</td>
<td class="hideSmall">48</td>
<td> 
        -20

 </td>
<td class="points">21</td>
<td class="form hideMed">
<ul>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12055" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 12 March 2016</span>
<span class="teamName">NOR</span>
<span class="badge-20 t7604"></span>
<span class="score">0 <span>-</span>1</span>
<span class="badge-20 t8967"></span>
<span class="teamName">SWA</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12066" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 19 March 2016</span>
<span class="teamName">NOR</span>
<span class="badge-20 t7604"></span>
<span class="score">2 <span>-</span>3</span>
<span class="badge-20 t6747"></span>
<span class="teamName">STK</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12081" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 9 April 2016</span>
<span class="teamName">SOU</span>
<span class="badge-20 t7588"></span>
<span class="score">3 <span>-</span>1</span>
<span class="badge-20 t7604"></span>
<span class="teamName">NOR</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12092" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Friday 22 April 2016</span>
<span class="teamName">NOR</span>
<span class="badge-20 t7604"></span>
<span class="score">2 <span>-</span>3</span>
<span class="badge-20 t6752"></span>
<span class="teamName">MUN</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12103" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 30 April 2016</span>
<span class="teamName">DER</span>
<span class="badge-20 t6757"></span>
<span class="score">2 <span>-</span>1</span>
<span class="badge-20 t7604"></span>
<span class="teamName">NOR</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
</ul>
<td class="nextMatchCol hideMed">
</td>
</td>
</tr>
<tr class="expandable" data-filtered-table-row-expander="321">
<td colspan="13">
<a class="expandableTeam" href="/clubs/14/Norwich-City/overview">
<span class="badge-50 t7604"></span>
<span class="teamName">Norwich City</span>
</a>
<div class="expandableFixtures">
<div class="resultWidget">
<div class="label"><strong>Recent Result</strong> - Saturday 12 March 2016</div>
<a class="matchAbridged pre" href="/match/12103">
<span class="teamName">DER</span>
<span class="badge-20 t6757"></span>
<span class="score">2 <span>-</span>1</span>
<span class="badge-20 t7604"></span>
<span class="teamName">NOR</span>
<span class="icn arrow-right"></span>
</a>
</div>
<div class="btnContainer">
<a class="btn-highlight" href="/clubs/14/Norwich-City/overview" role="btn">Visit <span class="visuallyHidden">Norwich City </span>Club Page<span class="icn arrow-right-w"></span></a>
</div>
</div>
<div class="teamPerformanceStandingsArea" style="display:none;">
<header>
<h3 class="subHeader left">Performance Chart</h3>
<a class="btn right" href="/stats/comparison">Compare against another team<span class="icn arrow-right"></span></a>
</header>
<div class="teamPerformanceStandingsContainer"></div>
</div>
</td>
</tr>
<tr class="" data-compseason="35" data-filtered-entry-size="12" data-filtered-table-row="323" data-filtered-table-row-abbr="323" data-filtered-table-row-name="Southampton" data-filtered-table-row-opta="t7588">
<td class="pos" tabindex="0">
<span class="value">11</span>
</td>
<td class="team" scope="row">
<a href="/clubs/20/Southampton/overview"><span alt="" class="badge-25 t7588"></span><span class="long">Southampton</span><span class="short">SOU</span></a>
</td>
<td>22</td>
<td>4</td>
<td>3</td>
<td>15</td>
<td class="hideSmall">34</td>
<td class="hideSmall">57</td>
<td> 
        -23

 </td>
<td class="points">15</td>
<td class="form hideMed">
<ul>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12081" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 9 April 2016</span>
<span class="teamName">SOU</span>
<span class="badge-20 t7588"></span>
<span class="score">3 <span>-</span>1</span>
<span class="badge-20 t7604"></span>
<span class="teamName">NOR</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12087" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 16 April 2016</span>
<span class="teamName">STK</span>
<span class="badge-20 t6747"></span>
<span class="score">1 <span>-</span>0</span>
<span class="badge-20 t7588"></span>
<span class="teamName">SOU</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12093" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Friday 22 April 2016</span>
<span class="teamName">SOU</span>
<span class="badge-20 t7588"></span>
<span class="score">0 <span>-</span>1</span>
<span class="badge-20 t6757"></span>
<span class="teamName">DER</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12106" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 30 April 2016</span>
<span class="teamName">MUN</span>
<span class="badge-20 t6752"></span>
<span class="score">1 <span>-</span>0</span>
<span class="badge-20 t7588"></span>
<span class="teamName">SOU</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12114" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 7 May 2016</span>
<span class="teamName">NEW</span>
<span class="badge-20 t7603"></span>
<span class="score">4 <span>-</span>1</span>
<span class="badge-20 t7588"></span>
<span class="teamName">SOU</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
</ul>
<td class="nextMatchCol hideMed">
</td>
</td>
</tr>
<tr class="expandable" data-filtered-table-row-expander="323">
<td colspan="13">
<a class="expandableTeam" href="/clubs/20/Southampton/overview">
<span class="badge-50 t7588"></span>
<span class="teamName">Southampton</span>
</a>
<div class="expandableFixtures">
<div class="resultWidget">
<div class="label"><strong>Recent Result</strong> - Saturday 9 April 2016</div>
<a class="matchAbridged pre" href="/match/12114">
<span class="teamName">NEW</span>
<span class="badge-20 t7603"></span>
<span class="score">4 <span>-</span>1</span>
<span class="badge-20 t7588"></span>
<span class="teamName">SOU</span>
<span class="icn arrow-right"></span>
</a>
</div>
<div class="btnContainer">
<a class="btn-highlight" href="/clubs/20/Southampton/overview" role="btn">Visit <span class="visuallyHidden">Southampton </span>Club Page<span class="icn arrow-right-w"></span></a>
</div>
</div>
<div class="teamPerformanceStandingsArea" style="display:none;">
<header>
<h3 class="subHeader left">Performance Chart</h3>
<a class="btn right" href="/stats/comparison">Compare against another team<span class="icn arrow-right"></span></a>
</header>
<div class="teamPerformanceStandingsContainer"></div>
</div>
</td>
</tr>
<tr class="" data-compseason="35" data-filtered-entry-size="12" data-filtered-table-row="326" data-filtered-table-row-abbr="326" data-filtered-table-row-name="Swansea" data-filtered-table-row-opta="t8967">
<td class="pos" tabindex="0">
<span class="value">12</span>
</td>
<td class="team" scope="row">
<a href="/clubs/45/Swansea-City/overview"><span alt="" class="badge-25 t8967"></span><span class="long">Swansea City</span><span class="short">SWA</span></a>
</td>
<td>22</td>
<td>3</td>
<td>4</td>
<td>15</td>
<td class="hideSmall">25</td>
<td class="hideSmall">54</td>
<td> 
        -29

 </td>
<td class="points">13</td>
<td class="form hideMed">
<ul>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12055" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 12 March 2016</span>
<span class="teamName">NOR</span>
<span class="badge-20 t7604"></span>
<span class="score">0 <span>-</span>1</span>
<span class="badge-20 t8967"></span>
<span class="teamName">SWA</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12082" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 9 April 2016</span>
<span class="teamName">SWA</span>
<span class="badge-20 t8967"></span>
<span class="score">2 <span>-</span>1</span>
<span class="badge-20 t6747"></span>
<span class="teamName">STK</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12084" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 16 April 2016</span>
<span class="teamName">DER</span>
<span class="badge-20 t6757"></span>
<span class="score">3 <span>-</span>4</span>
<span class="badge-20 t8967"></span>
<span class="teamName">SWA</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="draw button-tooltip" id="Tooltip" role="tooltip" tabindex="0">D
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12094" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 23 April 2016</span>
<span class="teamName">BHA</span>
<span class="badge-20 t7552"></span>
<span class="score">3 <span>-</span>3</span>
<span class="badge-20 t8967"></span>
<span class="teamName">SWA</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/12110" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 30 April 2016</span>
<span class="teamName">SWA</span>
<span class="badge-20 t8967"></span>
<span class="score">2 <span>-</span>1</span>
<span class="badge-20 t7603"></span>
<span class="teamName">NEW</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
</ul>
<td class="nextMatchCol hideMed">
</td>
</td>
</tr>
<tr class="expandable" data-filtered-table-row-expander="326">
<td colspan="13">
<a class="expandableTeam" href="/clubs/45/Swansea-City/overview">
<span class="badge-50 t8967"></span>
<span class="teamName">Swansea City</span>
</a>
<div class="expandableFixtures">
<div class="resultWidget">
<div class="label"><strong>Recent Result</strong> - Saturday 12 March 2016</div>
<a class="matchAbridged pre" href="/match/12110">
<span class="teamName">SWA</span>
<span class="badge-20 t8967"></span>
<span class="score">2 <span>-</span>1</span>
<span class="badge-20 t7603"></span>
<span class="teamName">NEW</span>
<span class="icn arrow-right"></span>
</a>
</div>
<div class="btnContainer">
<a class="btn-highlight" href="/clubs/45/Swansea-City/overview" role="btn">Visit <span class="visuallyHidden">Swansea City </span>Club Page<span class="icn arrow-right-w"></span></a>
</div>
</div>
<div class="teamPerformanceStandingsArea" style="display:none;">
<header>
<h3 class="subHeader left">Performance Chart</h3>
<a class="btn right" href="/stats/comparison">Compare against another team<span class="icn arrow-right"></span></a>
</header>
<div class="teamPerformanceStandingsContainer"></div>
</div>
</td>
</tr>
</tbody>
</table>
</div>]
>>> table('thread')
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    table('thread')
TypeError: 'ResultSet' object is not callable
>>> table('thread')table=soup.find('div' ,{'class':"table wrapper col-12"})
SyntaxError: invalid syntax
>>> table=soup.find('div' ,{'class':"table wrapper col-12"})
>>> table('thread')
[]
>>> len(table)
2
>>> table
<div class="table wrapper col-12">
<table>
<summary class="visuallyHidden">This table charts the Premier League teams</summary>
<thead>
<tr>
<th class="revealMoreHeader text-centre" scope="col" style="display:none;">More</th>
<th class="text-centre" scope="col">
<div class="thFull">Position</div>
<div class="thShort">Pos</div>
</th>
<th class="team" scope="col">Club</th>
<th scope="col">
<div class="thFull">Played</div>
<div class="thShort">Pl</div>
</th>
<th scope="col">
<div class="thFull">Won</div>
<div class="thShort">W</div>
</th>
<th scope="col">
<div class="thFull">Drawn</div>
<div class="thShort">D</div>
</th>
<th scope="col">
<div class="thFull">Lost</div>
<div class="thShort">L</div>
</th>
<th class="hideSmall" scope="col"><abbr title="Goals For">GF</abbr></th>
<th class="hideSmall" scope="col"><abbr title="Goals Against">GA</abbr></th>
<th scope="col"><abbr title="Goal Difference">GD</abbr></th>
<th class="points" scope="col">
<div class="thFull">Points</div>
<div class="thShort">Pts</div>
</th>
<th class="teamForm hideMed" scope="col">Form</th>
<th class="hideMed text-centre" scope="col">Next</th>
</tr>
</thead>
<tbody class="tableBodyContainer">
<tr class="tableDark" data-compseason="79" data-filtered-entry-size="20" data-filtered-table-row="11" data-filtered-table-row-abbr="11" data-filtered-table-row-name="Manchester City" data-filtered-table-row-opta="t43">
<td class="revealMore" role="button" style="display:none;" tabindex="0">
<div class="icn chevron-down-g"></div>
</td>
<td class="pos button-tooltip" id="Tooltip" role="tooltip" tabindex="0">
<span class="value">1</span>
<span class="movement none">
<span class="tooltipContainer tooltip-left" role="tooltip">
<span class="tooltip-content">Previous Position
                            <span class="resultHighlight">
                                1
                            </span>
</span>
</span>
</span>
</td>
<td class="team" scope="row">
<a href="/clubs/11/Manchester-City/overview"><span alt="" class="badge-25 t43"></span><span class="long">Manchester City</span><span class="short">MCI</span></a>
</td>
<td>7</td>
<td>6</td>
<td>1</td>
<td>0</td>
<td class="hideSmall">22</td>
<td class="hideSmall">2</td>
<td> 
        +20

 </td>
<td class="points">19</td>
<td class="form hideMed">
<ul>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/22362" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 26 August 2017</span>
<span class="teamName">BOU</span>
<span class="badge-20 t91"></span>
<span class="score">1 <span>-</span>2</span>
<span class="badge-20 t43"></span>
<span class="teamName">MCI</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/22377" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 9 September 2017</span>
<span class="teamName">MCI</span>
<span class="badge-20 t43"></span>
<span class="score">5 <span>-</span>0</span>
<span class="badge-20 t14"></span>
<span class="teamName">LIV</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/22390" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 16 September 2017</span>
<span class="teamName">WAT</span>
<span class="badge-20 t57"></span>
<span class="score">0 <span>-</span>6</span>
<span class="badge-20 t43"></span>
<span class="teamName">MCI</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/22397" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 23 September 2017</span>
<span class="teamName">MCI</span>
<span class="badge-20 t43"></span>
<span class="score">5 <span>-</span>0</span>
<span class="badge-20 t31"></span>
<span class="teamName">CRY</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/22404" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 30 September 2017</span>
<span class="teamName">CHE</span>
<span class="badge-20 t8"></span>
<span class="score">0 <span>-</span>1</span>
<span class="badge-20 t43"></span>
<span class="teamName">MCI</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
</ul>
<td class="nextMatchCol hideMed">
<span class="button-tooltip" id="Tooltip" role="tooltip" tabindex="0">
<span class="nextMatch"><span class="badge-20 t110"><span class="visuallyHidden">Stoke City</span></span></span>
<a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/22417" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 14 October 2017</span>
<span class="teamName">MCI</span>
<span class="badge-20 t43"></span>
<time>15:00</time>
<span class="badge-20 t110"></span>
<span class="teamName">STK</span>
<span class="icn arrow-right"></span>
</div></span>
</a></span></td></td></tr></tbody></table></div>
>>> table('tr')
[<tr>
<th class="revealMoreHeader text-centre" scope="col" style="display:none;">More</th>
<th class="text-centre" scope="col">
<div class="thFull">Position</div>
<div class="thShort">Pos</div>
</th>
<th class="team" scope="col">Club</th>
<th scope="col">
<div class="thFull">Played</div>
<div class="thShort">Pl</div>
</th>
<th scope="col">
<div class="thFull">Won</div>
<div class="thShort">W</div>
</th>
<th scope="col">
<div class="thFull">Drawn</div>
<div class="thShort">D</div>
</th>
<th scope="col">
<div class="thFull">Lost</div>
<div class="thShort">L</div>
</th>
<th class="hideSmall" scope="col"><abbr title="Goals For">GF</abbr></th>
<th class="hideSmall" scope="col"><abbr title="Goals Against">GA</abbr></th>
<th scope="col"><abbr title="Goal Difference">GD</abbr></th>
<th class="points" scope="col">
<div class="thFull">Points</div>
<div class="thShort">Pts</div>
</th>
<th class="teamForm hideMed" scope="col">Form</th>
<th class="hideMed text-centre" scope="col">Next</th>
</tr>, <tr class="tableDark" data-compseason="79" data-filtered-entry-size="20" data-filtered-table-row="11" data-filtered-table-row-abbr="11" data-filtered-table-row-name="Manchester City" data-filtered-table-row-opta="t43">
<td class="revealMore" role="button" style="display:none;" tabindex="0">
<div class="icn chevron-down-g"></div>
</td>
<td class="pos button-tooltip" id="Tooltip" role="tooltip" tabindex="0">
<span class="value">1</span>
<span class="movement none">
<span class="tooltipContainer tooltip-left" role="tooltip">
<span class="tooltip-content">Previous Position
                            <span class="resultHighlight">
                                1
                            </span>
</span>
</span>
</span>
</td>
<td class="team" scope="row">
<a href="/clubs/11/Manchester-City/overview"><span alt="" class="badge-25 t43"></span><span class="long">Manchester City</span><span class="short">MCI</span></a>
</td>
<td>7</td>
<td>6</td>
<td>1</td>
<td>0</td>
<td class="hideSmall">22</td>
<td class="hideSmall">2</td>
<td> 
        +20

 </td>
<td class="points">19</td>
<td class="form hideMed">
<ul>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/22362" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 26 August 2017</span>
<span class="teamName">BOU</span>
<span class="badge-20 t91"></span>
<span class="score">1 <span>-</span>2</span>
<span class="badge-20 t43"></span>
<span class="teamName">MCI</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/22377" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 9 September 2017</span>
<span class="teamName">MCI</span>
<span class="badge-20 t43"></span>
<span class="score">5 <span>-</span>0</span>
<span class="badge-20 t14"></span>
<span class="teamName">LIV</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/22390" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 16 September 2017</span>
<span class="teamName">WAT</span>
<span class="badge-20 t57"></span>
<span class="score">0 <span>-</span>6</span>
<span class="badge-20 t43"></span>
<span class="teamName">MCI</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/22397" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 23 September 2017</span>
<span class="teamName">MCI</span>
<span class="badge-20 t43"></span>
<span class="score">5 <span>-</span>0</span>
<span class="badge-20 t31"></span>
<span class="teamName">CRY</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/22404" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 30 September 2017</span>
<span class="teamName">CHE</span>
<span class="badge-20 t8"></span>
<span class="score">0 <span>-</span>1</span>
<span class="badge-20 t43"></span>
<span class="teamName">MCI</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
</ul>
<td class="nextMatchCol hideMed">
<span class="button-tooltip" id="Tooltip" role="tooltip" tabindex="0">
<span class="nextMatch"><span class="badge-20 t110"><span class="visuallyHidden">Stoke City</span></span></span>
<a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/22417" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 14 October 2017</span>
<span class="teamName">MCI</span>
<span class="badge-20 t43"></span>
<time>15:00</time>
<span class="badge-20 t110"></span>
<span class="teamName">STK</span>
<span class="icn arrow-right"></span>
</div></span>
</a></span></td></td></tr>]
>>> table=soup.findAll('div' ,{'class':"table wrapper col-12"})
>>> len(table)
8
>>> table[0].find('tbody',{'class':"tableBodyContainer"})
<tbody class="tableBodyContainer">
<tr class="tableDark" data-compseason="79" data-filtered-entry-size="20" data-filtered-table-row="11" data-filtered-table-row-abbr="11" data-filtered-table-row-name="Manchester City" data-filtered-table-row-opta="t43">
<td class="revealMore" role="button" style="display:none;" tabindex="0">
<div class="icn chevron-down-g"></div>
</td>
<td class="pos button-tooltip" id="Tooltip" role="tooltip" tabindex="0">
<span class="value">1</span>
<span class="movement none">
<span class="tooltipContainer tooltip-left" role="tooltip">
<span class="tooltip-content">Previous Position
                            <span class="resultHighlight">
                                1
                            </span>
</span>
</span>
</span>
</td>
<td class="team" scope="row">
<a href="/clubs/11/Manchester-City/overview"><span alt="" class="badge-25 t43"></span><span class="long">Manchester City</span><span class="short">MCI</span></a>
</td>
<td>7</td>
<td>6</td>
<td>1</td>
<td>0</td>
<td class="hideSmall">22</td>
<td class="hideSmall">2</td>
<td> 
        +20

 </td>
<td class="points">19</td>
<td class="form hideMed">
<ul>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/22362" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 26 August 2017</span>
<span class="teamName">BOU</span>
<span class="badge-20 t91"></span>
<span class="score">1 <span>-</span>2</span>
<span class="badge-20 t43"></span>
<span class="teamName">MCI</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/22377" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 9 September 2017</span>
<span class="teamName">MCI</span>
<span class="badge-20 t43"></span>
<span class="score">5 <span>-</span>0</span>
<span class="badge-20 t14"></span>
<span class="teamName">LIV</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/22390" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 16 September 2017</span>
<span class="teamName">WAT</span>
<span class="badge-20 t57"></span>
<span class="score">0 <span>-</span>6</span>
<span class="badge-20 t43"></span>
<span class="teamName">MCI</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/22397" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 23 September 2017</span>
<span class="teamName">MCI</span>
<span class="badge-20 t43"></span>
<span class="score">5 <span>-</span>0</span>
<span class="badge-20 t31"></span>
<span class="teamName">CRY</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/22404" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 30 September 2017</span>
<span class="teamName">CHE</span>
<span class="badge-20 t8"></span>
<span class="score">0 <span>-</span>1</span>
<span class="badge-20 t43"></span>
<span class="teamName">MCI</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
</ul>
<td class="nextMatchCol hideMed">
<span class="button-tooltip" id="Tooltip" role="tooltip" tabindex="0">
<span class="nextMatch"><span class="badge-20 t110"><span class="visuallyHidden">Stoke City</span></span></span>
<a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/22417" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 14 October 2017</span>
<span class="teamName">MCI</span>
<span class="badge-20 t43"></span>
<time>15:00</time>
<span class="badge-20 t110"></span>
<span class="teamName">STK</span>
<span class="icn arrow-right"></span>
</div></span>
</a></span></td></td></tr></tbody>
>>> table[1].find('tbody',{'class':"tableBodyContainer"})
<tbody class="tableBodyContainer">
<tr class="tableDark" data-compseason="39" data-filtered-entry-size="12" data-filtered-table-row="387" data-filtered-table-row-abbr="387" data-filtered-table-row-name="Man Utd" data-filtered-table-row-opta="t6826">
<td class="pos" tabindex="0">
<span class="value">1</span>
</td>
<td class="team" scope="row">
<a href="/clubs/12/Manchester-United/overview"><span alt="" class="badge-25 t6826"></span><span class="long">Manchester United</span><span class="short">MUN</span></a>
</td>
<td>22</td>
<td>15</td>
<td>3</td>
<td>4</td>
<td class="hideSmall">44</td>
<td class="hideSmall">19</td>
<td> 
        +25

 </td>
<td class="points">48</td>
<td class="form hideMed">
<ul>
<li class="draw button-tooltip" id="Tooltip" role="tooltip" tabindex="0">D
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13736" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 4 April 2016</span>
<span class="teamName">MUN</span>
<span class="badge-20 t6826"></span>
<span class="score">1 <span>-</span>1</span>
<span class="badge-20 t7140"></span>
<span class="teamName">CHE</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13749" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 11 April 2016</span>
<span class="teamName">MUN</span>
<span class="badge-20 t6826"></span>
<span class="score">1 <span>-</span>0</span>
<span class="badge-20 t7138"></span>
<span class="teamName">MID</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13760" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Tuesday 19 April 2016</span>
<span class="teamName">TOT</span>
<span class="badge-20 t1175"></span>
<span class="score">2 <span>-</span>3</span>
<span class="badge-20 t6826"></span>
<span class="teamName">MUN</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13764" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 25 April 2016</span>
<span class="teamName">SOU</span>
<span class="badge-20 t1189"></span>
<span class="score">2 <span>-</span>1</span>
<span class="badge-20 t6826"></span>
<span class="teamName">MUN</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13768" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Friday 6 May 2016</span>
<span class="teamName">CHE</span>
<span class="badge-20 t7140"></span>
<span class="score">0 <span>-</span>1</span>
<span class="badge-20 t6826"></span>
<span class="teamName">MUN</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
</ul>
<td class="nextMatchCol hideMed">
</td>
</td>
</tr>
<tr class="expandable" data-filtered-table-row-expander="387">
<td colspan="13">
<a class="expandableTeam" href="/clubs/12/Manchester-United/overview">
<span class="badge-50 t6826"></span>
<span class="teamName">Manchester United</span>
</a>
<div class="expandableFixtures">
<div class="resultWidget">
<div class="label"><strong>Recent Result</strong> - Monday 4 April 2016</div>
<a class="matchAbridged pre" href="/match/13768">
<span class="teamName">CHE</span>
<span class="badge-20 t7140"></span>
<span class="score">0 <span>-</span>1</span>
<span class="badge-20 t6826"></span>
<span class="teamName">MUN</span>
<span class="icn arrow-right"></span>
</a>
</div>
<div class="btnContainer">
<a class="btn-highlight" href="/clubs/12/Manchester-United/overview" role="btn">Visit <span class="visuallyHidden">Manchester United </span>Club Page<span class="icn arrow-right-w"></span></a>
</div>
</div>
<div class="teamPerformanceStandingsArea" style="display:none;">
<header>
<h3 class="subHeader left">Performance Chart</h3>
<a class="btn right" href="/stats/comparison">Compare against another team<span class="icn arrow-right"></span></a>
</header>
<div class="teamPerformanceStandingsContainer"></div>
</div>
</td>
</tr>
<tr class="" data-compseason="39" data-filtered-entry-size="12" data-filtered-table-row="355" data-filtered-table-row-abbr="355" data-filtered-table-row-name="Sunderland" data-filtered-table-row-opta="t819">
<td class="pos" tabindex="0">
<span class="value">2</span>
</td>
<td class="team" scope="row">
<a href="/clubs/29/Sunderland/overview"><span alt="" class="badge-25 t819"></span><span class="long">Sunderland</span><span class="short">SUN</span></a>
</td>
<td>22</td>
<td>13</td>
<td>4</td>
<td>5</td>
<td class="hideSmall">38</td>
<td class="hideSmall">20</td>
<td> 
        +18

 </td>
<td class="points">43</td>
<td class="form hideMed">
<ul>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13705" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 7 March 2016</span>
<span class="teamName">SUN</span>
<span class="badge-20 t819"></span>
<span class="score">3 <span>-</span>2</span>
<span class="badge-20 t7592"></span>
<span class="teamName">EVE</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="draw button-tooltip" id="Tooltip" role="tooltip" tabindex="0">D
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13715" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Saturday 12 March 2016</span>
<span class="teamName">MCI</span>
<span class="badge-20 t1050"></span>
<span class="score">1 <span>-</span>1</span>
<span class="badge-20 t819"></span>
<span class="teamName">SUN</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13727" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 21 March 2016</span>
<span class="teamName">MID</span>
<span class="badge-20 t7138"></span>
<span class="score">0 <span>-</span>1</span>
<span class="badge-20 t819"></span>
<span class="teamName">SUN</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="draw button-tooltip" id="Tooltip" role="tooltip" tabindex="0">D
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13732" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Sunday 3 April 2016</span>
<span class="teamName">SUN</span>
<span class="badge-20 t819"></span>
<span class="score">2 <span>-</span>2</span>
<span class="badge-20 t1189"></span>
<span class="teamName">SOU</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13752" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 11 April 2016</span>
<span class="teamName">TOT</span>
<span class="badge-20 t1175"></span>
<span class="score">3 <span>-</span>1</span>
<span class="badge-20 t819"></span>
<span class="teamName">SUN</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
</ul>
<td class="nextMatchCol hideMed">
</td>
</td>
</tr>
<tr class="expandable" data-filtered-table-row-expander="355">
<td colspan="13">
<a class="expandableTeam" href="/clubs/29/Sunderland/overview">
<span class="badge-50 t819"></span>
<span class="teamName">Sunderland</span>
</a>
<div class="expandableFixtures">
<div class="resultWidget">
<div class="label"><strong>Recent Result</strong> - Monday 7 March 2016</div>
<a class="matchAbridged pre" href="/match/13752">
<span class="teamName">TOT</span>
<span class="badge-20 t1175"></span>
<span class="score">3 <span>-</span>1</span>
<span class="badge-20 t819"></span>
<span class="teamName">SUN</span>
<span class="icn arrow-right"></span>
</a>
</div>
<div class="btnContainer">
<a class="btn-highlight" href="/clubs/29/Sunderland/overview" role="btn">Visit <span class="visuallyHidden">Sunderland </span>Club Page<span class="icn arrow-right-w"></span></a>
</div>
</div>
<div class="teamPerformanceStandingsArea" style="display:none;">
<header>
<h3 class="subHeader left">Performance Chart</h3>
<a class="btn right" href="/stats/comparison">Compare against another team<span class="icn arrow-right"></span></a>
</header>
<div class="teamPerformanceStandingsContainer"></div>
</div>
</td>
</tr>
<tr class="" data-compseason="39" data-filtered-entry-size="12" data-filtered-table-row="339" data-filtered-table-row-abbr="339" data-filtered-table-row-name="Everton" data-filtered-table-row-opta="t7592">
<td class="pos" tabindex="0">
<span class="value">3</span>
</td>
<td class="team" scope="row">
<a href="/clubs/7/Everton/overview"><span alt="" class="badge-25 t7592"></span><span class="long">Everton</span><span class="short">EVE</span></a>
</td>
<td>22</td>
<td>10</td>
<td>7</td>
<td>5</td>
<td class="hideSmall">35</td>
<td class="hideSmall">27</td>
<td> 
        +8

 </td>
<td class="points">37</td>
<td class="form hideMed">
<ul>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13737" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 4 April 2016</span>
<span class="teamName">NOR</span>
<span class="badge-20 t6920"></span>
<span class="score">1 <span>-</span>2</span>
<span class="badge-20 t7592"></span>
<span class="teamName">EVE</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13747" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 11 April 2016</span>
<span class="teamName">EVE</span>
<span class="badge-20 t7592"></span>
<span class="score">2 <span>-</span>0</span>
<span class="badge-20 t7140"></span>
<span class="teamName">CHE</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13757" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 18 April 2016</span>
<span class="teamName">EVE</span>
<span class="badge-20 t7592"></span>
<span class="score">1 <span>-</span>0</span>
<span class="badge-20 t1050"></span>
<span class="teamName">MCI</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13761" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 25 April 2016</span>
<span class="teamName">EVE</span>
<span class="badge-20 t7592"></span>
<span class="score">3 <span>-</span>1</span>
<span class="badge-20 t8755"></span>
<span class="teamName">LEI</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="draw button-tooltip" id="Tooltip" role="tooltip" tabindex="0">D
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13766" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 2 May 2016</span>
<span class="teamName">CHE</span>
<span class="badge-20 t7140"></span>
<span class="score">0 <span>-</span>0</span>
<span class="badge-20 t7592"></span>
<span class="teamName">EVE</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
</ul>
<td class="nextMatchCol hideMed">
</td>
</td>
</tr>
<tr class="expandable" data-filtered-table-row-expander="339">
<td colspan="13">
<a class="expandableTeam" href="/clubs/7/Everton/overview">
<span class="badge-50 t7592"></span>
<span class="teamName">Everton</span>
</a>
<div class="expandableFixtures">
<div class="resultWidget">
<div class="label"><strong>Recent Result</strong> - Monday 4 April 2016</div>
<a class="matchAbridged pre" href="/match/13766">
<span class="teamName">CHE</span>
<span class="badge-20 t7140"></span>
<span class="score">0 <span>-</span>0</span>
<span class="badge-20 t7592"></span>
<span class="teamName">EVE</span>
<span class="icn arrow-right"></span>
</a>
</div>
<div class="btnContainer">
<a class="btn-highlight" href="/clubs/7/Everton/overview" role="btn">Visit <span class="visuallyHidden">Everton </span>Club Page<span class="icn arrow-right-w"></span></a>
</div>
</div>
<div class="teamPerformanceStandingsArea" style="display:none;">
<header>
<h3 class="subHeader left">Performance Chart</h3>
<a class="btn right" href="/stats/comparison">Compare against another team<span class="icn arrow-right"></span></a>
</header>
<div class="teamPerformanceStandingsContainer"></div>
</div>
</td>
</tr>
<tr class="" data-compseason="39" data-filtered-entry-size="12" data-filtered-table-row="381" data-filtered-table-row-abbr="381" data-filtered-table-row-name="Man City" data-filtered-table-row-opta="t1050">
<td class="pos" tabindex="0">
<span class="value">4</span>
</td>
<td class="team" scope="row">
<a href="/clubs/11/Manchester-City/overview"><span alt="" class="badge-25 t1050"></span><span class="long">Manchester City</span><span class="short">MCI</span></a>
</td>
<td>22</td>
<td>10</td>
<td>4</td>
<td>8</td>
<td class="hideSmall">35</td>
<td class="hideSmall">26</td>
<td> 
        +9

 </td>
<td class="points">34</td>
<td class="form hideMed">
<ul>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13731" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Friday 1 April 2016</span>
<span class="teamName">MID</span>
<span class="badge-20 t7138"></span>
<span class="score">3 <span>-</span>1</span>
<span class="badge-20 t1050"></span>
<span class="teamName">MCI</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13751" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 11 April 2016</span>
<span class="teamName">RDG</span>
<span class="badge-20 t7608"></span>
<span class="score">0 <span>-</span>3</span>
<span class="badge-20 t1050"></span>
<span class="teamName">MCI</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13757" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 18 April 2016</span>
<span class="teamName">EVE</span>
<span class="badge-20 t7592"></span>
<span class="score">1 <span>-</span>0</span>
<span class="badge-20 t1050"></span>
<span class="teamName">MCI</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13769" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Friday 6 May 2016</span>
<span class="teamName">MCI</span>
<span class="badge-20 t1050"></span>
<span class="score">2 <span>-</span>0</span>
<span class="badge-20 t7139"></span>
<span class="teamName">LIV</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13770" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 9 May 2016</span>
<span class="teamName">MCI</span>
<span class="badge-20 t1050"></span>
<span class="score">0 <span>-</span>1</span>
<span class="badge-20 t7140"></span>
<span class="teamName">CHE</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
</ul>
<td class="nextMatchCol hideMed">
</td>
</td>
</tr>
<tr class="expandable" data-filtered-table-row-expander="381">
<td colspan="13">
<a class="expandableTeam" href="/clubs/11/Manchester-City/overview">
<span class="badge-50 t1050"></span>
<span class="teamName">Manchester City</span>
</a>
<div class="expandableFixtures">
<div class="resultWidget">
<div class="label"><strong>Recent Result</strong> - Friday 1 April 2016</div>
<a class="matchAbridged pre" href="/match/13770">
<span class="teamName">MCI</span>
<span class="badge-20 t1050"></span>
<span class="score">0 <span>-</span>1</span>
<span class="badge-20 t7140"></span>
<span class="teamName">CHE</span>
<span class="icn arrow-right"></span>
</a>
</div>
<div class="btnContainer">
<a class="btn-highlight" href="/clubs/11/Manchester-City/overview" role="btn">Visit <span class="visuallyHidden">Manchester City </span>Club Page<span class="icn arrow-right-w"></span></a>
</div>
</div>
<div class="teamPerformanceStandingsArea" style="display:none;">
<header>
<h3 class="subHeader left">Performance Chart</h3>
<a class="btn right" href="/stats/comparison">Compare against another team<span class="icn arrow-right"></span></a>
</header>
<div class="teamPerformanceStandingsContainer"></div>
</div>
</td>
</tr>
<tr class="" data-compseason="39" data-filtered-entry-size="12" data-filtered-table-row="336" data-filtered-table-row-abbr="336" data-filtered-table-row-name="Chelsea" data-filtered-table-row-opta="t7140">
<td class="pos" tabindex="0">
<span class="value">5</span>
</td>
<td class="team" scope="row">
<a href="/clubs/4/Chelsea/overview"><span alt="" class="badge-25 t7140"></span><span class="long">Chelsea</span><span class="short">CHE</span></a>
</td>
<td>22</td>
<td>9</td>
<td>6</td>
<td>7</td>
<td class="hideSmall">34</td>
<td class="hideSmall">30</td>
<td> 
        +4

 </td>
<td class="points">33</td>
<td class="form hideMed">
<ul>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13763" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 25 April 2016</span>
<span class="teamName">MID</span>
<span class="badge-20 t7138"></span>
<span class="score">1 <span>-</span>3</span>
<span class="badge-20 t7140"></span>
<span class="teamName">CHE</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="draw button-tooltip" id="Tooltip" role="tooltip" tabindex="0">D
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13766" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 2 May 2016</span>
<span class="teamName">CHE</span>
<span class="badge-20 t7140"></span>
<span class="score">0 <span>-</span>0</span>
<span class="badge-20 t7592"></span>
<span class="teamName">EVE</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13768" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Friday 6 May 2016</span>
<span class="teamName">CHE</span>
<span class="badge-20 t7140"></span>
<span class="score">0 <span>-</span>1</span>
<span class="badge-20 t6826"></span>
<span class="teamName">MUN</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13770" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 9 May 2016</span>
<span class="teamName">MCI</span>
<span class="badge-20 t1050"></span>
<span class="score">0 <span>-</span>1</span>
<span class="badge-20 t7140"></span>
<span class="teamName">CHE</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13772" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Thursday 12 May 2016</span>
<span class="teamName">LEI</span>
<span class="badge-20 t8755"></span>
<span class="score">3 <span>-</span>0</span>
<span class="badge-20 t7140"></span>
<span class="teamName">CHE</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
</ul>
<td class="nextMatchCol hideMed">
</td>
</td>
</tr>
<tr class="expandable" data-filtered-table-row-expander="336">
<td colspan="13">
<a class="expandableTeam" href="/clubs/4/Chelsea/overview">
<span class="badge-50 t7140"></span>
<span class="teamName">Chelsea</span>
</a>
<div class="expandableFixtures">
<div class="resultWidget">
<div class="label"><strong>Recent Result</strong> - Monday 25 April 2016</div>
<a class="matchAbridged pre" href="/match/13772">
<span class="teamName">LEI</span>
<span class="badge-20 t8755"></span>
<span class="score">3 <span>-</span>0</span>
<span class="badge-20 t7140"></span>
<span class="teamName">CHE</span>
<span class="icn arrow-right"></span>
</a>
</div>
<div class="btnContainer">
<a class="btn-highlight" href="/clubs/4/Chelsea/overview" role="btn">Visit <span class="visuallyHidden">Chelsea </span>Club Page<span class="icn arrow-right-w"></span></a>
</div>
</div>
<div class="teamPerformanceStandingsArea" style="display:none;">
<header>
<h3 class="subHeader left">Performance Chart</h3>
<a class="btn right" href="/stats/comparison">Compare against another team<span class="icn arrow-right"></span></a>
</header>
<div class="teamPerformanceStandingsContainer"></div>
</div>
</td>
</tr>
<tr class="" data-compseason="39" data-filtered-entry-size="12" data-filtered-table-row="352" data-filtered-table-row-abbr="352" data-filtered-table-row-name="Southampton" data-filtered-table-row-opta="t1189">
<td class="pos" tabindex="0">
<span class="value">6</span>
</td>
<td class="team" scope="row">
<a href="/clubs/20/Southampton/overview"><span alt="" class="badge-25 t1189"></span><span class="long">Southampton</span><span class="short">SOU</span></a>
</td>
<td>22</td>
<td>8</td>
<td>6</td>
<td>8</td>
<td class="hideSmall">39</td>
<td class="hideSmall">40</td>
<td> 
        -1

 </td>
<td class="points">30</td>
<td class="form hideMed">
<ul>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13719" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 14 March 2016</span>
<span class="teamName">MID</span>
<span class="badge-20 t7138"></span>
<span class="score">1 <span>-</span>3</span>
<span class="badge-20 t1189"></span>
<span class="teamName">SOU</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13725" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Sunday 20 March 2016</span>
<span class="teamName">LIV</span>
<span class="badge-20 t7139"></span>
<span class="score">0 <span>-</span>5</span>
<span class="badge-20 t1189"></span>
<span class="teamName">SOU</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="draw button-tooltip" id="Tooltip" role="tooltip" tabindex="0">D
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13732" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Sunday 3 April 2016</span>
<span class="teamName">SUN</span>
<span class="badge-20 t819"></span>
<span class="score">2 <span>-</span>2</span>
<span class="badge-20 t1189"></span>
<span class="teamName">SOU</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13758" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 18 April 2016</span>
<span class="teamName">SOU</span>
<span class="badge-20 t1189"></span>
<span class="score">3 <span>-</span>2</span>
<span class="badge-20 t6920"></span>
<span class="teamName">NOR</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13764" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 25 April 2016</span>
<span class="teamName">SOU</span>
<span class="badge-20 t1189"></span>
<span class="score">2 <span>-</span>1</span>
<span class="badge-20 t6826"></span>
<span class="teamName">MUN</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
</ul>
<td class="nextMatchCol hideMed">
</td>
</td>
</tr>
<tr class="expandable" data-filtered-table-row-expander="352">
<td colspan="13">
<a class="expandableTeam" href="/clubs/20/Southampton/overview">
<span class="badge-50 t1189"></span>
<span class="teamName">Southampton</span>
</a>
<div class="expandableFixtures">
<div class="resultWidget">
<div class="label"><strong>Recent Result</strong> - Monday 14 March 2016</div>
<a class="matchAbridged pre" href="/match/13764">
<span class="teamName">SOU</span>
<span class="badge-20 t1189"></span>
<span class="score">2 <span>-</span>1</span>
<span class="badge-20 t6826"></span>
<span class="teamName">MUN</span>
<span class="icn arrow-right"></span>
</a>
</div>
<div class="btnContainer">
<a class="btn-highlight" href="/clubs/20/Southampton/overview" role="btn">Visit <span class="visuallyHidden">Southampton </span>Club Page<span class="icn arrow-right-w"></span></a>
</div>
</div>
<div class="teamPerformanceStandingsArea" style="display:none;">
<header>
<h3 class="subHeader left">Performance Chart</h3>
<a class="btn right" href="/stats/comparison">Compare against another team<span class="icn arrow-right"></span></a>
</header>
<div class="teamPerformanceStandingsContainer"></div>
</div>
</td>
</tr>
<tr class="" data-compseason="39" data-filtered-entry-size="12" data-filtered-table-row="344" data-filtered-table-row-abbr="344" data-filtered-table-row-name="Liverpool" data-filtered-table-row-opta="t7139">
<td class="pos" tabindex="0">
<span class="value">7</span>
</td>
<td class="team" scope="row">
<a href="/clubs/10/Liverpool/overview"><span alt="" class="badge-25 t7139"></span><span class="long">Liverpool</span><span class="short">LIV</span></a>
</td>
<td>22</td>
<td>8</td>
<td>4</td>
<td>10</td>
<td class="hideSmall">26</td>
<td class="hideSmall">37</td>
<td> 
        -11

 </td>
<td class="points">28</td>
<td class="form hideMed">
<ul>
<li class="draw button-tooltip" id="Tooltip" role="tooltip" tabindex="0">D
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13712" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Friday 11 March 2016</span>
<span class="teamName">LIV</span>
<span class="badge-20 t7139"></span>
<span class="score">1 <span>-</span>1</span>
<span class="badge-20 t6826"></span>
<span class="teamName">MUN</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13725" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Sunday 20 March 2016</span>
<span class="teamName">LIV</span>
<span class="badge-20 t7139"></span>
<span class="score">0 <span>-</span>5</span>
<span class="badge-20 t1189"></span>
<span class="teamName">SOU</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13735" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 4 April 2016</span>
<span class="teamName">LEI</span>
<span class="badge-20 t8755"></span>
<span class="score">0 <span>-</span>2</span>
<span class="badge-20 t7139"></span>
<span class="teamName">LIV</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13762" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 25 April 2016</span>
<span class="teamName">LIV</span>
<span class="badge-20 t7139"></span>
<span class="score">2 <span>-</span>1</span>
<span class="badge-20 t6920"></span>
<span class="teamName">NOR</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13769" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Friday 6 May 2016</span>
<span class="teamName">MCI</span>
<span class="badge-20 t1050"></span>
<span class="score">2 <span>-</span>0</span>
<span class="badge-20 t7139"></span>
<span class="teamName">LIV</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
</ul>
<td class="nextMatchCol hideMed">
</td>
</td>
</tr>
<tr class="expandable" data-filtered-table-row-expander="344">
<td colspan="13">
<a class="expandableTeam" href="/clubs/10/Liverpool/overview">
<span class="badge-50 t7139"></span>
<span class="teamName">Liverpool</span>
</a>
<div class="expandableFixtures">
<div class="resultWidget">
<div class="label"><strong>Recent Result</strong> - Friday 11 March 2016</div>
<a class="matchAbridged pre" href="/match/13769">
<span class="teamName">MCI</span>
<span class="badge-20 t1050"></span>
<span class="score">2 <span>-</span>0</span>
<span class="badge-20 t7139"></span>
<span class="teamName">LIV</span>
<span class="icn arrow-right"></span>
</a>
</div>
<div class="btnContainer">
<a class="btn-highlight" href="/clubs/10/Liverpool/overview" role="btn">Visit <span class="visuallyHidden">Liverpool </span>Club Page<span class="icn arrow-right-w"></span></a>
</div>
</div>
<div class="teamPerformanceStandingsArea" style="display:none;">
<header>
<h3 class="subHeader left">Performance Chart</h3>
<a class="btn right" href="/stats/comparison">Compare against another team<span class="icn arrow-right"></span></a>
</header>
<div class="teamPerformanceStandingsContainer"></div>
</div>
</td>
</tr>
<tr class="" data-compseason="39" data-filtered-entry-size="12" data-filtered-table-row="383" data-filtered-table-row-abbr="383" data-filtered-table-row-name="Spurs" data-filtered-table-row-opta="t1175">
<td class="pos" tabindex="0">
<span class="value">8</span>
</td>
<td class="team" scope="row">
<a href="/clubs/21/Tottenham-Hotspur/overview"><span alt="" class="badge-25 t1175"></span><span class="long">Tottenham Hotspur</span><span class="short">TOT</span></a>
</td>
<td>22</td>
<td>7</td>
<td>6</td>
<td>9</td>
<td class="hideSmall">44</td>
<td class="hideSmall">43</td>
<td> 
        +1

 </td>
<td class="points">27</td>
<td class="form hideMed">
<ul>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13714" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Friday 11 March 2016</span>
<span class="teamName">TOT</span>
<span class="badge-20 t1175"></span>
<span class="score">1 <span>-</span>2</span>
<span class="badge-20 t6920"></span>
<span class="teamName">NOR</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13722" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Friday 18 March 2016</span>
<span class="teamName">LEI</span>
<span class="badge-20 t8755"></span>
<span class="score">0 <span>-</span>3</span>
<span class="badge-20 t1175"></span>
<span class="teamName">TOT</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13741" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Wednesday 6 April 2016</span>
<span class="teamName">TOT</span>
<span class="badge-20 t1175"></span>
<span class="score">1 <span>-</span>2</span>
<span class="badge-20 t7138"></span>
<span class="teamName">MID</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13752" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 11 April 2016</span>
<span class="teamName">TOT</span>
<span class="badge-20 t1175"></span>
<span class="score">3 <span>-</span>1</span>
<span class="badge-20 t819"></span>
<span class="teamName">SUN</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13760" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Tuesday 19 April 2016</span>
<span class="teamName">TOT</span>
<span class="badge-20 t1175"></span>
<span class="score">2 <span>-</span>3</span>
<span class="badge-20 t6826"></span>
<span class="teamName">MUN</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
</ul>
<td class="nextMatchCol hideMed">
</td>
</td>
</tr>
<tr class="expandable" data-filtered-table-row-expander="383">
<td colspan="13">
<a class="expandableTeam" href="/clubs/21/Tottenham-Hotspur/overview">
<span class="badge-50 t1175"></span>
<span class="teamName">Tottenham Hotspur</span>
</a>
<div class="expandableFixtures">
<div class="resultWidget">
<div class="label"><strong>Recent Result</strong> - Friday 11 March 2016</div>
<a class="matchAbridged pre" href="/match/13760">
<span class="teamName">TOT</span>
<span class="badge-20 t1175"></span>
<span class="score">2 <span>-</span>3</span>
<span class="badge-20 t6826"></span>
<span class="teamName">MUN</span>
<span class="icn arrow-right"></span>
</a>
</div>
<div class="btnContainer">
<a class="btn-highlight" href="/clubs/21/Tottenham-Hotspur/overview" role="btn">Visit <span class="visuallyHidden">Tottenham Hotspur </span>Club Page<span class="icn arrow-right-w"></span></a>
</div>
</div>
<div class="teamPerformanceStandingsArea" style="display:none;">
<header>
<h3 class="subHeader left">Performance Chart</h3>
<a class="btn right" href="/stats/comparison">Compare against another team<span class="icn arrow-right"></span></a>
</header>
<div class="teamPerformanceStandingsContainer"></div>
</div>
</td>
</tr>
<tr class="" data-compseason="39" data-filtered-entry-size="12" data-filtered-table-row="351" data-filtered-table-row-abbr="351" data-filtered-table-row-name="Reading" data-filtered-table-row-opta="t7608">
<td class="pos" tabindex="0">
<span class="value">9</span>
</td>
<td class="team" scope="row">
<a href="/clubs/40/Reading/overview"><span alt="" class="badge-25 t7608"></span><span class="long">Reading</span><span class="short">RDG</span></a>
</td>
<td>22</td>
<td>7</td>
<td>6</td>
<td>9</td>
<td class="hideSmall">34</td>
<td class="hideSmall">40</td>
<td> 
        -6

 </td>
<td class="points">27</td>
<td class="form hideMed">
<ul>
<li class="draw button-tooltip" id="Tooltip" role="tooltip" tabindex="0">D
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13699" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Thursday 3 March 2016</span>
<span class="teamName">RDG</span>
<span class="badge-20 t7608"></span>
<span class="score">1 <span>-</span>1</span>
<span class="badge-20 t1175"></span>
<span class="teamName">TOT</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13704" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 7 March 2016</span>
<span class="teamName">RDG</span>
<span class="badge-20 t7608"></span>
<span class="score">1 <span>-</span>3</span>
<span class="badge-20 t7140"></span>
<span class="teamName">CHE</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13718" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 14 March 2016</span>
<span class="teamName">EVE</span>
<span class="badge-20 t7592"></span>
<span class="score">0 <span>-</span>2</span>
<span class="badge-20 t7608"></span>
<span class="teamName">RDG</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="draw button-tooltip" id="Tooltip" role="tooltip" tabindex="0">D
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13728" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 21 March 2016</span>
<span class="teamName">NOR</span>
<span class="badge-20 t6920"></span>
<span class="score">4 <span>-</span>4</span>
<span class="badge-20 t7608"></span>
<span class="teamName">RDG</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13751" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 11 April 2016</span>
<span class="teamName">RDG</span>
<span class="badge-20 t7608"></span>
<span class="score">0 <span>-</span>3</span>
<span class="badge-20 t1050"></span>
<span class="teamName">MCI</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
</ul>
<td class="nextMatchCol hideMed">
</td>
</td>
</tr>
<tr class="expandable" data-filtered-table-row-expander="351">
<td colspan="13">
<a class="expandableTeam" href="/clubs/40/Reading/overview">
<span class="badge-50 t7608"></span>
<span class="teamName">Reading</span>
</a>
<div class="expandableFixtures">
<div class="resultWidget">
<div class="label"><strong>Recent Result</strong> - Thursday 3 March 2016</div>
<a class="matchAbridged pre" href="/match/13751">
<span class="teamName">RDG</span>
<span class="badge-20 t7608"></span>
<span class="score">0 <span>-</span>3</span>
<span class="badge-20 t1050"></span>
<span class="teamName">MCI</span>
<span class="icn arrow-right"></span>
</a>
</div>
<div class="btnContainer">
<a class="btn-highlight" href="/clubs/40/Reading/overview" role="btn">Visit <span class="visuallyHidden">Reading </span>Club Page<span class="icn arrow-right-w"></span></a>
</div>
</div>
<div class="teamPerformanceStandingsArea" style="display:none;">
<header>
<h3 class="subHeader left">Performance Chart</h3>
<a class="btn right" href="/stats/comparison">Compare against another team<span class="icn arrow-right"></span></a>
</header>
<div class="teamPerformanceStandingsContainer"></div>
</div>
</td>
</tr>
<tr class="" data-compseason="39" data-filtered-entry-size="12" data-filtered-table-row="343" data-filtered-table-row-abbr="343" data-filtered-table-row-name="Leicester" data-filtered-table-row-opta="t8755">
<td class="pos" tabindex="0">
<span class="value">10</span>
</td>
<td class="team" scope="row">
<a href="/clubs/26/Leicester-City/overview"><span alt="" class="badge-25 t8755"></span><span class="long">Leicester City</span><span class="short">LEI</span></a>
</td>
<td>22</td>
<td>6</td>
<td>3</td>
<td>13</td>
<td class="hideSmall">25</td>
<td class="hideSmall">48</td>
<td> 
        -23

 </td>
<td class="points">21</td>
<td class="form hideMed">
<ul>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13722" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Friday 18 March 2016</span>
<span class="teamName">LEI</span>
<span class="badge-20 t8755"></span>
<span class="score">0 <span>-</span>3</span>
<span class="badge-20 t1175"></span>
<span class="teamName">TOT</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13735" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 4 April 2016</span>
<span class="teamName">LEI</span>
<span class="badge-20 t8755"></span>
<span class="score">0 <span>-</span>2</span>
<span class="badge-20 t7139"></span>
<span class="teamName">LIV</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13748" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 11 April 2016</span>
<span class="teamName">LEI</span>
<span class="badge-20 t8755"></span>
<span class="score">0 <span>-</span>1</span>
<span class="badge-20 t6920"></span>
<span class="teamName">NOR</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13761" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 25 April 2016</span>
<span class="teamName">EVE</span>
<span class="badge-20 t7592"></span>
<span class="score">3 <span>-</span>1</span>
<span class="badge-20 t8755"></span>
<span class="teamName">LEI</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13772" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Thursday 12 May 2016</span>
<span class="teamName">LEI</span>
<span class="badge-20 t8755"></span>
<span class="score">3 <span>-</span>0</span>
<span class="badge-20 t7140"></span>
<span class="teamName">CHE</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
</ul>
<td class="nextMatchCol hideMed">
</td>
</td>
</tr>
<tr class="expandable" data-filtered-table-row-expander="343">
<td colspan="13">
<a class="expandableTeam" href="/clubs/26/Leicester-City/overview">
<span class="badge-50 t8755"></span>
<span class="teamName">Leicester City</span>
</a>
<div class="expandableFixtures">
<div class="resultWidget">
<div class="label"><strong>Recent Result</strong> - Friday 18 March 2016</div>
<a class="matchAbridged pre" href="/match/13772">
<span class="teamName">LEI</span>
<span class="badge-20 t8755"></span>
<span class="score">3 <span>-</span>0</span>
<span class="badge-20 t7140"></span>
<span class="teamName">CHE</span>
<span class="icn arrow-right"></span>
</a>
</div>
<div class="btnContainer">
<a class="btn-highlight" href="/clubs/26/Leicester-City/overview" role="btn">Visit <span class="visuallyHidden">Leicester City </span>Club Page<span class="icn arrow-right-w"></span></a>
</div>
</div>
<div class="teamPerformanceStandingsArea" style="display:none;">
<header>
<h3 class="subHeader left">Performance Chart</h3>
<a class="btn right" href="/stats/comparison">Compare against another team<span class="icn arrow-right"></span></a>
</header>
<div class="teamPerformanceStandingsContainer"></div>
</div>
</td>
</tr>
<tr class="" data-compseason="39" data-filtered-entry-size="12" data-filtered-table-row="345" data-filtered-table-row-abbr="345" data-filtered-table-row-name="Middlesbrough" data-filtered-table-row-opta="t7138">
<td class="pos" tabindex="0">
<span class="value">11</span>
</td>
<td class="team" scope="row">
<a href="/clubs/13/Middlesbrough/overview"><span alt="" class="badge-25 t7138"></span><span class="long">Middlesbrough</span><span class="short">MID</span></a>
</td>
<td>22</td>
<td>5</td>
<td>5</td>
<td>12</td>
<td class="hideSmall">33</td>
<td class="hideSmall">37</td>
<td> 
        -4

 </td>
<td class="points">20</td>
<td class="form hideMed">
<ul>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13727" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 21 March 2016</span>
<span class="teamName">MID</span>
<span class="badge-20 t7138"></span>
<span class="score">0 <span>-</span>1</span>
<span class="badge-20 t819"></span>
<span class="teamName">SUN</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13731" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Friday 1 April 2016</span>
<span class="teamName">MID</span>
<span class="badge-20 t7138"></span>
<span class="score">3 <span>-</span>1</span>
<span class="badge-20 t1050"></span>
<span class="teamName">MCI</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13741" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Wednesday 6 April 2016</span>
<span class="teamName">TOT</span>
<span class="badge-20 t1175"></span>
<span class="score">1 <span>-</span>2</span>
<span class="badge-20 t7138"></span>
<span class="teamName">MID</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13749" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 11 April 2016</span>
<span class="teamName">MUN</span>
<span class="badge-20 t6826"></span>
<span class="score">1 <span>-</span>0</span>
<span class="badge-20 t7138"></span>
<span class="teamName">MID</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13763" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 25 April 2016</span>
<span class="teamName">MID</span>
<span class="badge-20 t7138"></span>
<span class="score">1 <span>-</span>3</span>
<span class="badge-20 t7140"></span>
<span class="teamName">CHE</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
</ul>
<td class="nextMatchCol hideMed">
</td>
</td>
</tr>
<tr class="expandable" data-filtered-table-row-expander="345">
<td colspan="13">
<a class="expandableTeam" href="/clubs/13/Middlesbrough/overview">
<span class="badge-50 t7138"></span>
<span class="teamName">Middlesbrough</span>
</a>
<div class="expandableFixtures">
<div class="resultWidget">
<div class="label"><strong>Recent Result</strong> - Monday 21 March 2016</div>
<a class="matchAbridged pre" href="/match/13763">
<span class="teamName">MID</span>
<span class="badge-20 t7138"></span>
<span class="score">1 <span>-</span>3</span>
<span class="badge-20 t7140"></span>
<span class="teamName">CHE</span>
<span class="icn arrow-right"></span>
</a>
</div>
<div class="btnContainer">
<a class="btn-highlight" href="/clubs/13/Middlesbrough/overview" role="btn">Visit <span class="visuallyHidden">Middlesbrough </span>Club Page<span class="icn arrow-right-w"></span></a>
</div>
</div>
<div class="teamPerformanceStandingsArea" style="display:none;">
<header>
<h3 class="subHeader left">Performance Chart</h3>
<a class="btn right" href="/stats/comparison">Compare against another team<span class="icn arrow-right"></span></a>
</header>
<div class="teamPerformanceStandingsContainer"></div>
</div>
</td>
</tr>
<tr class="" data-compseason="39" data-filtered-entry-size="12" data-filtered-table-row="347" data-filtered-table-row-abbr="347" data-filtered-table-row-name="Norwich" data-filtered-table-row-opta="t6920">
<td class="pos" tabindex="0">
<span class="value">12</span>
</td>
<td class="team" scope="row">
<a href="/clubs/14/Norwich-City/overview"><span alt="" class="badge-25 t6920"></span><span class="long">Norwich City</span><span class="short">NOR</span></a>
</td>
<td>22</td>
<td>5</td>
<td>4</td>
<td>13</td>
<td class="hideSmall">30</td>
<td class="hideSmall">50</td>
<td> 
        -20

 </td>
<td class="points">19</td>
<td class="form hideMed">
<ul>
<li class="draw button-tooltip" id="Tooltip" role="tooltip" tabindex="0">D
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13728" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 21 March 2016</span>
<span class="teamName">NOR</span>
<span class="badge-20 t6920"></span>
<span class="score">4 <span>-</span>4</span>
<span class="badge-20 t7608"></span>
<span class="teamName">RDG</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13737" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 4 April 2016</span>
<span class="teamName">NOR</span>
<span class="badge-20 t6920"></span>
<span class="score">1 <span>-</span>2</span>
<span class="badge-20 t7592"></span>
<span class="teamName">EVE</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="win button-tooltip" id="Tooltip" role="tooltip" tabindex="0">W
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13748" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 11 April 2016</span>
<span class="teamName">LEI</span>
<span class="badge-20 t8755"></span>
<span class="score">0 <span>-</span>1</span>
<span class="badge-20 t6920"></span>
<span class="teamName">NOR</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13758" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 18 April 2016</span>
<span class="teamName">SOU</span>
<span class="badge-20 t1189"></span>
<span class="score">3 <span>-</span>2</span>
<span class="badge-20 t6920"></span>
<span class="teamName">NOR</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
<li class="lose button-tooltip" id="Tooltip" role="tooltip" tabindex="0">L
                        <a class="tooltipContainer linkable tooltip-link tooltip-right" href="/match/13762" role="tooltip">
<span class="tooltip-content">
<div class="matchAbridged">
<span class="matchInfo">Monday 25 April 2016</span>
<span class="teamName">LIV</span>
<span class="badge-20 t7139"></span>
<span class="score">2 <span>-</span>1</span>
<span class="badge-20 t6920"></span>
<span class="teamName">NOR</span>
<span class="icn arrow-right"></span>
</div>
</span>
</a>
</li>
</ul>
<td class="nextMatchCol hideMed">
</td>
</td>
</tr>
<tr class="expandable" data-filtered-table-row-expander="347">
<td colspan="13">
<a class="expandableTeam" href="/clubs/14/Norwich-City/overview">
<span class="badge-50 t6920"></span>
<span class="teamName">Norwich City</span>
</a>
<div class="expandableFixtures">
<div class="resultWidget">
<div class="label"><strong>Recent Result</strong> - Monday 21 March 2016</div>
<a class="matchAbridged pre" href="/match/13762">
<span class="teamName">LIV</span>
<span class="badge-20 t7139"></span>
<span class="score">2 <span>-</span>1</span>
<span class="badge-20 t6920"></span>
<span class="teamName">NOR</span>
<span class="icn arrow-right"></span>
</a>
</div>
<div class="btnContainer">
<a class="btn-highlight" href="/clubs/14/Norwich-City/overview" role="btn">Visit <span class="visuallyHidden">Norwich City </span>Club Page<span class="icn arrow-right-w"></span></a>
</div>
</div>
<div class="teamPerformanceStandingsArea" style="display:none;">
<header>
<h3 class="subHeader left">Performance Chart</h3>
<a class="btn right" href="/stats/comparison">Compare against another team<span class="icn arrow-right"></span></a>
</header>
<div class="teamPerformanceStandingsContainer"></div>
</div>
</td>
</tr>
</tbody>
>>> 
