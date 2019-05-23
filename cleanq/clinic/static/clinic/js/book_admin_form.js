$( document ).ready(function() {
  $('input[type=file]').each(function() {
    $(this).after(' <input type="checkbox" name="clear_image_'+$(this).attr('name')+'"/> Clear');
  });

  $("#show_results").click(function () {
    base_dir = '/catalog/api/get_images/'
    end = $("#id_title").val()
    $.ajax({
      url: base_dir.concat(end),
      dataType: 'json',
      success: function (data) {
        let rows =  '';
        data.items.forEach(item => {
        rows += `
        <div class='img_cover_border'>
          <div class='img_cover_div'>
          <img class='img img_cover' src="${item.link}">
          </div>
          <div class='img_cover_link'>
            <a target="_blank" href="${item.link}" download="`+$("#id_title").val()+`">
              <button type='button' class='img_cover btn'>
              Download
              </button>
            </a>
          </div>
        </div>
        `;
        });
        $("#results").append(rows)
      }
    });
  });
  $(document).on("click", '.img_cover_border', function(event) {
    $(this).addClass('select_border').siblings().removeClass('select_border')
});
});

