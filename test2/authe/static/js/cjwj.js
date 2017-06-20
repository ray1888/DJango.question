
</script>
		var t_id=1
		
		
		var appendMulti=function(){
			console.log("1111111111111111111111");
			var div11=document.createElement("div");
			div11.setAttribute("id","tmk"+t_id);
			div11.setAttribute("class","tm");
			var div22=document.createElement("div");
			div22.setAttribute("class","alert alert-warning");
			var num=2;
			var op_num=prompt("请输入选项的个数:","");
			var insert=document.getElementById("insert");
			var h1=document.createElement("h3");
			var text1=document.createTextNode(t_id +"."+"标题"+"("+"multi"+")");
			h1.appendChild(text1);
			h1.setAttribute("id",t_id+"TI");
			var s_id=0;
			
			var br=document.createElement("br");
			var input0=document.createElement("input");
			var text2=document.createTextNode("please input option content");
			input0.appendChild(text2);
			input0.setAttribute("id",t_id+"_"+"0");
			input0.setAttribute("name",t_id+"_"+"0");
			input0.setAttribute("class","form-control");
			input0.setAttribute("aria-describedby","basic-addon1");
			/*
			insert.appendChild(h1,br);
			insert.appendChild(input0,br);
			*/
			div11.appendChild(h1,br);
			div11.appendChild(input0,br);
			
			var p1=document.createElement("p");
			var inputg=document.createElement("input");
			var text_p1=document.createTextNode("type");
			inputg.setAttribute("id",t_id+"_"+"1");
			inputg.setAttribute("name",t_id+"_"+"1");
			inputg.setAttribute("value","多选");
			inputg.setAttribute("class","form-control");
			inputg.setAttribute("aria-describedby","basic-addon1");
			p1.appendChild(text_p1);
			/*p1.appendChild(inputg);
			insert.appendChild(p1);
			insert.appendChild(inputg);
			*/
			div11.appendChild(p1);
			div11.appendChild(inputg);
			

			var h2=document.createElement("h3");
			var text2=document.createTextNode("选项");
			h2.appendChild(text2);
			div11.appendChild(h2,br);
			//insert.appendChild(h2,br);
			var selectionarr= ["a","b","c","d","e","f","g","h","i","j","k","l","m","n"];
			for(i=0;i<op_num;i=i+1){
				var h3=document.createElement("h3");
				var inputu=document.createElement("input");
				var br1=document.createElement("br");
				var text_h3 =document.createTextNode(selectionarr[i]);
				h3.setAttribute("id",t_id+"_"+selectionarr[i]);
				h3.appendChild(text_h3);
				s_id=s_id+1;
				u=i;
				inputu.setAttribute("id",t_id+"_"+num);
				inputu.setAttribute("name",t_id+"_"+num);
				inputu.setAttribute("class","form-control");
				inputu.setAttribute("aria-describedby","basic-addon1");
				num=num+1;
				/*
				insert.appendChild(h3);
				insert.appendChild(inputu);
				insert.appendChild(br1);
				*/
				div22.appendChild(h3);
				div22.appendChild(inputu);
				div22.appendChild(br1);
			};
			
			div11.appendChild(div22);
			div11.appendChild(br);
			div11.appendChild(br);
			div11.appendChild(br);
			div11.appendChild(br);
			insert.appendChild(div11);
			/*
			var button2=document.createElement("button");
			var text4 = document.createTextNode("增加选项");
			button2.setAttribute("id","button2"+t_id);
			button2.appendChild(text4);
			insert.appendChild(button2);
			*/
			t_id = t_id + 1;
			
			

		};

		$("#").click(function(){
				$("#Div1").hide();
			});
		
		
		
			
		var appendSigle=function(){
			var div11=document.createElement("div");
			div11.setAttribute("id","tmk"+t_id);
			div11.setAttribute("class","tm");
			var div22=document.createElement("div");
			div22.setAttribute("class","alert alert-info");
			var op_num=prompt("请输入选项的个数:","");
			var num=2;
			var insert=document.getElementById("insert");
			var h1=document.createElement("h3");
			var text1=document.createTextNode(t_id +"."+"标题"+"("+"single"+")");
			h1.appendChild(text1);
			/*h1.setAttribute("id",t_id+"_"+"0");*/
			var s_id=0;
			
			var br=document.createElement("br");
			var input0=document.createElement("input");
			var text2=document.createTextNode("please input option content");
			input0.appendChild(text2);
			input0.setAttribute("name",t_id+"_"+"0");
			input0.setAttribute("class","form-control");
			input0.setAttribute("aria-describedby","basic-addon1");
			/*
			insert.appendChild(h1,br);
			insert.appendChild(input0,br);
			*/
			div11.appendChild(h1,br);
			div11.appendChild(input0,br);
			
			var p1=document.createElement("p");
			var inputg=document.createElement("input");
			var text_p1=document.createTextNode("type");
			inputg.setAttribute("id",t_id+"_"+"1");
			inputg.setAttribute("name",t_id+"_"+"1");
			inputg.setAttribute("value","单选");
			inputg.setAttribute("class","form-control");
			inputg.setAttribute("aria-describedby","basic-addon1");
			p1.appendChild(text_p1);
			/*
			insert.appendChild(p1);
			insert.appendChild(inputg);
			*/
			div11.appendChild(p1);
			div11.appendChild(inputg);
			
			var h2=document.createElement("h3")
			var text2=document.createTextNode("选项");
			h2.appendChild(text2);
			div11.appendChild(h2,br);
			//insert.appendChild(h2,br);
			var selectionarr= ["a","b","c","d","e","f","g","h","i","j","k","l","m","n"];
			for(i=0;i<op_num;i=i+1){
				u=i;
				var p=document.createElement("p");
				var inputu=document.createElement("input");
				var br1=document.createElement("br");
				var text_p=document.createTextNode(selectionarr[i]);
				p.setAttribute("id",t_id+"option"+selectionarr[i]);
				p.appendChild(text_p);


				/*s_id=s_id+1;*/

				inputu.setAttribute("id",t_id+"_"+num);
				inputu.setAttribute("name",t_id+"_"+num);
				inputu.setAttribute("class","form-control");
				inputu.setAttribute("aria-describedby","basic-addon1");
				inputu.type="text";
				num=num+1;
				/*
				insert.appendChild(p);
				insert.appendChild(inputu);
				insert.appendChild(br1);
				*/
				div22.appendChild(p);
				div22.appendChild(inputu);
				div22.appendChild(br1);
				
			};
			
			div11.appendChild(div22);
			div11.appendChild(br);
			div11.appendChild(br);
			div11.appendChild(br);
			div11.appendChild(br);
			div11.appendChild(br);
			insert.appendChild(div11);
			/*
			var button2=document.createElement("button");
			var text4 = document.createTextNode("增加选项");
			button2.setAttribute("id","button2"+t_id);
			button2.appendChild(text4);
			insert.appendChild(button2);
			*/
			t_id = t_id + 1;


		};
		
		
		var appendText = function (){
			var div11=document.createElement("div");
			div11.setAttribute("id","tmk"+t_id);
			div11.setAttribute("class","tm");
			var div22=document.createElement("div");
			div22.setAttribute("class","alert alert-danger");
			var insert=document.getElementById("insert");
			//var div1=document.createElement("div");
			//var div2=document.createElement("div");
			var h1=document.createElement("h3");
			var text1=document.createTextNode(t_id +"."+"标题"+"("+"text"+")");
			h1.appendChild(text1);
			h1.setAttribute("id",t_id);
			
			var br=document.createElement("br");
			var input0=document.createElement("input");
			var text2=document.createTextNode("please input option content");
			input0.appendChild(text2);
			input0.setAttribute("name",t_id+"_"+"0");
			input0.setAttribute("id",t_id+"_"+"0");
			input0.setAttribute("class","form-control");
			input0.setAttribute("aria-describedby","basic-addon1");
			div22.appendChild(h1,br);
			div22.appendChild(input0,br);
			//div1.appendChild(div2);

			var p1=document.createElement("p");
			var inputg=document.createElement("input");
			var text_p1=document.createTextNode("type");
			inputg.innerHtml="填空";
			inputg.setAttribute("id",t_id+"_"+"1");
			inputg.setAttribute("name",t_id+"_"+"1");
			inputg.setAttribute("value","填空");
			inputg.setAttribute("class","form-control");
			inputg.setAttribute("aria-describedby","basic-addon1");
			p1.appendChild(text_p1);
			/*
			insert.appendChild(p1);
			insert.appendChild(inputg);
			*/
			
			div11.appendChild(div22);
			div11.appendChild(p1);
			div11.appendChild(inputg);
			div11.appendChild(br);
			div11.appendChild(br);
			div11.appendChild(br);
			div11.appendChild(br);
			
			insert.appendChild(div11);
			//var div3=document.createElement("div");
			/*var h2=document.createElement("h3")
			var text2=document.createTextNode("答案");
			h2.appendChild(text2);
			insert.appendChild(h2,br);
			
			var textarea= document.createElement("input");
			textarea.setAttribute("id",t_id+"input"+text);
			textarea.type="text";
			textarea.setAttribute("name",t_id+"input"+text);
			insert.appendChild(textarea);*/
			

			
			t_id = t_id + 1;
			
			

		
		}
		
		var appendMat=function(){
			var div11=document.createElement("div");
			div11.setAttribute("id","tmk"+t_id);
			div11.setAttribute("class","tm");
			var num=3;
			var op_num=prompt("请输入选项的个数:","");
			var op_tm=prompt("请输入小题目的个数:","");
			var insert=document.getElementById("insert");
			var h1=document.createElement("h3");
			var text1=document.createTextNode(t_id +"."+"标题"+"("+"matrix"+")");
			h1.appendChild(text1);
			h1.setAttribute("id",t_id);
			
			var br=document.createElement("br");
			var input0=document.createElement("input");
			var text2=document.createTextNode("please input option content");
			input0.appendChild(text2);
			input0.setAttribute("name",t_id+"_"+"0");
			input0.setAttribute("id",t_id+"_"+"0");
			input0.setAttribute("class","form-control");
			input0.setAttribute("aria-describedby","basic-addon1");
			/*
			insert.appendChild(h1,br);
			insert.appendChild(input0,br);
			*/
			div11.appendChild(h1,br);
			div11.appendChild(input0,br);
			//div1.appendChild(div2);

			//var div3=document.createElement("div");

			var selectionarr= ["a","b","c","d","e","f","g","h","i","j","k","l","m","n"];

			var p1=document.createElement("p");
			var inputg=document.createElement("input");
			var text_p1=document.createTextNode("type");
			inputg.innerHtml="矩阵";
			inputg.setAttribute("id",t_id+"_"+"1");
			inputg.setAttribute("value","矩阵");
			inputg.setAttribute("name",t_id+"_"+"1");
			inputg.setAttribute("class","form-control");
			inputg.setAttribute("aria-describedby","basic-addon1");
			p1.appendChild(text_p1);
			/*
			insert.appendChild(p1);
			insert.appendChild(inputg);
			*/
			div11.appendChild(p1);
			div11.appendChild(inputg);
			
			
			var h3=document.createElement("h3")
			var text_h3 =document.createTextNode("选项");
			h3.appendChild(text_h3);
			//insert.appendChild(h3);
			div11.appendChild(h3);

			for (u=0;u<op_num;u++){
					var inputu =document.createElement("input");
					inputu.type="type";
					inputu.setAttribute("id",t_id+"_"+"2"+selectionarr[u]);
					inputu.setAttribute("name",t_id+"_"+"2"+selectionarr[u]);
					inputu.setAttribute("class","form-control");
					inputu.setAttribute("aria-describedby","basic-addon1");

					//insert.appendChild(inputu);
					div11.appendChild(inputu);
			};
			div11.appendChild(br);
			
			var h2=document.createElement("h3")
			var text2=document.createTextNode("小题目");
			h2.appendChild(text2);
			//insert.appendChild(h2,br);
			div11.appendChild(h2);
			div11.appendChild(br);
			
			for(i=0;i<op_tm;i++){
				var inputi=document.createElement("input");
				var br1=document.createElement("br");
				inputi.type="text";
				inputi.setAttribute("id",t_id+"_"+num);
				inputi.setAttribute("name",t_id+"_"+num);
				inputi.setAttribute("class","form-control");
				inputi.setAttribute("aria-describedby","basic-addon1");
				/*
				insert.appendChild(inputi);
				insert.appendChild(br1);
				*/
				div11.appendChild(inputi);
				div11.appendChild(br1);
				num=num+1;

					
				}
			
			//div11.appendChild(div22);
			//div11.appendChild(div33);
			div11.appendChild(br);
			div11.appendChild(br);
			div11.appendChild(br);
			div11.appendChild(br);
			div11.appendChild(br);
			insert.appendChild(div11);
			
			/*
			var button2=document.createElement("button");
			var text4 = document.createTextNode("增加选项");
			button2.setAttribute("id","button2"+t_id);
			button2.appendChild(text4);
			insert.appendChild(button2);
			*/
			t_id = t_id + 1;
			
			
			//div1.appendChild(div3);
			//div.appendChild(div1);
		};
		
		
		
		var canel=function(){
			t_id=t_id-1;
			$("#tmk"+t_id).remove();
		
		};
		
		var shuru=function(){
			var action=prompt("请输入你的操作:(温馨提示，只有插入和删除两个操作)","")
			if (action=="插入"){
				var th=prompt("请输入你需要插入的题号:","");
				action="charu";
				act=new Object();
				act.action=action;
				act.th=th;
				return act;
			}
			else if (action=="删除"){
				var th=prompt("请输入你需要删除的题号:","");
				action="shanchu";
				act=new Object();
				act.action=action;
				act.th=th;
				return act;
			}
			else{
				alert("输入错误，别老想搞事情！！！！")
			}
		
		
		};
		
		/*
		var xiugai=function(){
			var action1=new Object();
			action1=shuru();
			var th=action1.th;
			var action=action1.action;
			
			var len = $(".tm").size();
			var arr = [];
			console.log(len);
			var add_len=len+1;
			for(var index = 1; index < add_len; index++){//创建一个数字数组
				arr.push(index);
			}
			
			console.log(arr.length);
			console.log(arr);
			var ti_count=1;
			
			if (action=="shanchu"){
				$("#tmk"+th).remove();
			}
			
			$.each(arr, function(i){//循环得到不同的id的值
				var idValue = $(".tm").eq(i).attr("id");
				if ("tmk"+th > idValue){
					console.log("大于");
					ti_count+=1;
				}
				else{
					console.log("小于");
					
					
					if (action=="churu"){
						//val1.replace( /\d/ , ti_count+1);
						var xx_id=0;
						var val1=$("#"+ti_count).html();
						console.log(typeof(val1));
						var  val2=val1.split(".");
						console.log(val2[1]);
						tih=ti_count+1;
						var re_str=tih+val2[1];
						$("#"+ti_count).text(re_str);
						while (1){
							if ($("#"+ti_count+"_"+xx_id)) {
								alert(1);
								break;
							}
						
						}
						ti_count+=1;
					}
					
					else{
						var tih=Number(th)+1;
						var xx_id=0;						
						var Flag=1;
						console.log(tih);
						selectarr=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p'];
						var selnum=0;
						if ($("#"+tih+"_"+1)=="矩阵"){
							var tihm=Number(tih)-1;
							while(Flag){
								if ($("#"+tih+"_"+xx_id) !=[]){
									var val1=$("#"+tih).html();
									var val2=val1.split(".");
									var re_str=tihm+"."+val2[1];					
									$("#tmk"+tih).setAttribute("id","tmk"+tihm)
									$("#"+tih).text(re_str)
									$("#"+tih+"_"+xx_id).setAttribute("id",tihm+"_"+xx_id)
									xx_id+=1;
								}
								else if($("#"+tih+"_"+"0") ==[]){
									Flag=false;
								}
								else if($("#"+tih+"_"+xx_id+selectarr[selnum])!=[]){
									$("#"+tih+"_"+xx_id).setAttribute("id",tihm+"_"+xx_id);
									selnum+=1;
								}
								else if ($("#"+tih+"_"+xx_id+selectarr[selnum]) ==[]){
									xx_id+=1;
									selnum=0;
								}
								else{
									tih+=1;
									xx_id=0;
								}
							};
						}
						else{
							while (Flag){
								var tihm=Number(tih)-1;
								var s_tih=String(tih);
								console.log(tih);
								console.log(s_tih);
								if ($("#"+s_tih)!=[]){
									var val1=$("#"+s_tih).html();
									console.log(val1);
									var val2=val1.split(".");
									console.log(val2);
									var re_str=tihm+"."+val2[1];
									console.log(re_str);
									$("#"+tih).text(re_str);
									$("#"+tih).attr("id",tihm);
								}
								else if ($("#"+tih+"_"+xx_id)!=[]){
									
									$("#"+tih+"_"+xx_id).attr("id",tihm+"_"+xx_id);
									xx_id+=1;
								}
								else if($("#"+tih+"_"+"0")==[]){
									Flag=false;
								}
								else{
									$("#tmk"+tih).attr("id","tmk"+tihm);
									
									tih+=1;
									xx_id=0;
								}
							};
						}
						
						
					}
					
				}
			});
			
		}；
			
			*/
		
		};
</script>