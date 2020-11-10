d3.csv("/static/code.csv").then(function(data) {
  console.log(data);
var tagList=[]
data.forEach(d=>
  {
    tagList.push(d.Name)
  })

  /*var tagList= data.Name;*/
    console.log(tagList)

    var selectTag=d3.select("Form")
    tagList.forEach(tag=>{
        
       div= selectTag.append("div").attr("class", "form-group")
       div.append("label").attr("for","inputName").text(tag)
       div.append("input").attr("class", "form-control").attr("type", "text").attr("id", "inputval").attr("placeholder", tag).attr("name", tag).attr("required", "required")

    })

    selectTag.append("input").attr("type", "submit").attr("value", "submit").attr("class","btn btn-default")


    
    
});




    // Complete the event handler function for the form

  

