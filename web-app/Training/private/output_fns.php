<?

function do_html_header()								  // print an HTML header
{

?>

<html>

	<head>
		<title>Login Area</title>							
		
		<SCRIPT LANGUAGE="JavaScript">

			function changeDay()
			{
				f = document.formify;
				aDate = new Date();
				month=f.bdMonth.selectedIndex;
				year=f.bdYear.selectedIndex+1970;
				aDate.setMonth(month);
				aDate.setYear(year);
				f.bdDay.options.length=0;
				for (i=1; i<=31; i++)
				{
					aDate.setDate(i);
					if (month == aDate.getMonth())
					{
						opt = new Option(i);
				   		f.bdDay.options[f.bdDay.options.length] = opt;
					}
				}
			}

		</SCRIPT>
	</head>

<?

competition_header();

}

function do_html_footer()
{
  // print an HTML footer
?>
  </body>
  </html>
<?
}

function display_details_form()								// display html change details form
{
	$uinfo = get_member_details(1);
	$pinfo = get_member_details(2);
	$cinfo = get_member_details(3);
	$curyear = substr($pinfo[4], 0, 4);
	$curmonth = substr($pinfo[4], 5, 2);
	$curday = substr($pinfo[4], 8, 2);

?>

	<form action="change_details.php" name="formify" method=post>

	<h2><? ts_df_personal_info(); ?></h2>

	<table>   
		<tr>
			<td width="200">
				<? ts_df_name(); ?>
			</td>
			<td width="300">
				<input type="text" name="fname" size=30 maxlength=20 value="<? echo $pinfo[1]; ?>"/>
			</td>
		</tr>
		<tr>
			<td>
				<? ts_df_initials(); ?>
			</td>
			<td valign=top>
				<input type=text name=initials size=8 maxlength=8 value="<? echo $pinfo[2]; ?>"/>
			</td>
		</tr>
		<tr>
			<td>
				<? ts_df_surname(); ?>
			</td>
			<td valign=top>
				<input type="text" name="lname" size=30 maxlength=50 value="<? echo $pinfo[3]; ?>"/>
			</td>
		</tr>
		<tr>
			<td>
				<? ts_df_birth(); ?>
			</td>
			<td>
				<table>
					<tr>
						<td align="center">
							<? ts_df_year(); ?>
						</td>
						<td width="35">
						</td>
						<td align="center">
							<? ts_df_month(); ?>
						</td>
						<td width="35">
						</td>
						<td align="center">
							<? ts_df_day(); ?>
						</td>
					</tr>
					<tr>
						<td align="center">
							<select name="bdYear" size=1 onChange="changeDay();">
								<?
									for ($i=1970; $i<=1995; $i++)
									{
										$year=$i;
										if ($year==$curyear)
										{
											echo "<option value=$i selected=\"selected\"/> $i";
										} else
										{
											echo "<option value=$i/> $i";
										}
									}
								?>
							</select>
					 	</td>
						<td width="35">
						</td>
						<td align="center">
							<select name="bdMonth" size=1 onChange="changeDay();">
								<?
									for ($i=1; $i<=12; $i++)
									{
										$month=$i;
										if ($month == $curmonth)
										{
											echo "<option value=$i selected=\"selected\"/> $i";
										} else
										{
											echo "<option value=$i/> $i";
										}
									}
								?>
							</select>
						</td>
						<td width="35">
						</td>
						<td align="center">
							<select name="bdDay" size=1>";
								<?
									for ($i=1; $i<=31; $i++)
									{
										if ($i == $curday)
										{
											echo "<option value=$i selected=\"selected\"/> $i";
										} else
										{
											echo "<option value=$i/> $i";
										}
									}
								?>
							</select>
						</td>
						
					</tr>
				</table>
			</td>
		</tr>
		<tr>
			<td>
				<? ts_df_gender(); ?>
			</td>
			<td>
				<table width="100%">
					<tr>
					<td valign=top>
					<input type="radio" name="gender" value="f" <? if ($pinfo[5]=="f") echo "checked=\"checked\"";?>/>
					<? ts_df_female(); ?>
					</td>
					<td valign=top>
					<input type="radio" name="gender" value="m" <? if ($pinfo[5]=="m") echo "checked=\"checked\"";?>/>
					<? ts_df_male(); ?>
					</td>
					</tr>		
				</table>
			</td>
		</tr>
		<tr>
			<td>
				<? ts_df_language(); ?>
			</td>
			<td>
				<select name="langselect" size=1>
					<option value="English"  <? if ($pinfo[6]=="english") echo "selected=\"selected\"";?> >
						English
					</option>
					<option value="Afrikaans" <? if ($pinfo[6]=="afrikaans") echo "selected=\"selected\"";?> >
						Afrikaans
					</option>
					<option value="Xhosa" <? if ($pinfo[6]=="xhosa") echo "selected=\"selected\"";?> >
						Xhosa
					</option>
					<option value="Zulu" <? if ($pinfo[6]=="zulu") echo "selected=\"selected\"";?> >
						Zulu
					</option>
					<option value="Sotho" <? if ($pinfo[6]=="sotho") echo "selected=\"selected\"";?> >
						Sotho
					</option>
					<option value="Sepedi" <? if ($pinfo[6]=="sepedi") echo "selected=\"selected\"";?> >
						Sepedi
					</option>
					<option value="Xitsonga" <? if ($pinfo[6]=="xitsonga") echo "selected=\"selected\"";?> >
						Xitsonga
					</option>
					<option value="Venda" <? if ($pinfo[6]=="venda") echo "selected=\"selected\"";?> >
						Venda
					</option>
					<option value="Duits" <? if ($pinfo[6]=="duits") echo "selected=\"selected\"";?> >
						Duits
					</option>
					<option value="Setswana" <? if ($pinfo[6]=="setswana") echo "selected=\"selected\"";?> >
						Setswana
					</option>
					<option value="Other" <? if ($pinfo[6]=="other") echo "selected=\"selected\"";?> >
						Other
					</option>
				<select/>
			</td>
		</tr>
	</table>
	
	<h2><? ts_df_contact_info(); ?></h2>
	
	<table>
		<tr>
			<td width="200">
				<? ts_df_email(); ?>
			</td>
			<td>
				<input type="text" name="email" size=30 maxlength=100 value="<? echo $cinfo[1]; ?>" />
			</td>
		</tr>
		<tr>
			<td>
				<? ts_df_cell(); ?>
			</td>
			<td>
				<input type="text" name="cellphone" size=10 maxlength=10 value="<? echo $cinfo[2]; ?>" />
			</td>
		</tr>
		<tr>
			<td>
				<? ts_df_telephone(); ?>
			</td>
			<td>
				<input type="text" name="homenr" size=10 maxlength=10 value="<? echo $cinfo[3]; ?>" />
			</td>
		</tr>
		<tr>
			<td>
				<? ts_df_town(); ?>
			</td>
			<td>
				<input type="text" name="town" size=30 maxlength=30 value="<? echo $cinfo[5]; ?>" />
			</td>
		</tr>
		<tr>
			<td>
				<? ts_df_post_address(); ?>
			</td>
			<td>
				<textarea name="postadd" rows=3 cols=30><? echo $cinfo[4]; ?> </textarea>
			</td>
		</tr>				
		<tr>
			<td>
				<? ts_df_post_code(); ?>
			</td>
			<td>
				<input type="text" name="postcode" size=5 maxlength=7 value="<? echo $cinfo[6]; ?>" />
			</td>
		</tr>				
		<tr>
			<td>
				<? ts_df_school(); ?>
			</td>
			<td>
				<textarea name="school" rows=3 cols=30><? echo $cinfo[7]; ?></textarea>
			</td>
		</tr>
		<tr>
			<td>
				<? ts_df_grade(); ?>
			</td>
			<td>
				<select name="grade" size=1>
					<?
						for ($i=1; $i<=12; $i++)
						{
							if ($i == $cinfo[8])
							{
								echo "<option value=$i selected=\"selected\"/> $i";
							} else
							{
								echo "<option value=$i/> $i";
							}
						}
					?>
				</select>
			</td>
		</tr>			
	</table>

	<input type="hidden" name="web_language" value=<? ts_language(); ?>>

	<? ts_df_preferences(); ?>
	
	<table>
		<tr>
			<td width="90" valign=top>
				<input type="radio" name="anonymous" value="1" <? if ($uinfo[8]=="1") echo "checked=\"checked\"";?>/>
				<? ts_df_yes(); ?>
			</td>
			<td valign=top>
				<input type="radio" name="anonymous" value="0" <? if ($uinfo[8]=="0") echo "checked=\"checked\"";?>/>
				<? ts_df_no(); ?>
			</td>
		</tr>		
	</table>

	<br>
	
	<table>
		<tr>
			<td colspan=2 align=center>
				<input type=submit value=<? ts_details_button(); ?>>
			</td>
		</tr>
	</table>
	
	</form>
	
<?

};

function display_password_form()
{

?>

	<form action="change_passwd.php" method="post">
		<table align="center" width="380" cellpadding="2" cellspacing="0">
			<tr>
				<td>
					<? ts_pf_old(); ?>
				</td>
				<td>
					<input type="password" name="old_passwd" size="16" maxlength="16">
				</td>
			</tr>
			<tr>
				<td>
					<? ts_pf_new(); ?>
				</td>
				<td>
					<input type="password" name="new_passwd" size="16" maxlength="16">
				</td>
			</tr>
			<tr>
				<td>
					<? ts_pf_repeat(); ?>
				</td>
				<td>
					<input type="password" name="new_passwd2" size="16" maxlength="16">
				</td>
			</tr>
		</table>

		<br>
		
		<table align="center" width="380">
			<tr>
				<td colspan=2 align="center">
					<input type="submit" value=<? ts_password_button(); ?>>
				</td>
			</tr>
		</table>
		
		<input type="hidden" name="web_language" value=<? ts_language(); ?>>

	</form>

<?

};

?>
