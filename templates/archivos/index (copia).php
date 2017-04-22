{% extends 'base/base.html' %}
{% block content %}

<?php
// include 'Views/funciones.php';

?>
  <div class="row">
    <div class="col-lg-12">
      <h2 class="page-header"><?php echo str_replace('Colegios', 'Documentos', str_replace('/*', '', $path))?> </h2>
    </div>
    
    <div class="col-lg-12">
        <?php  
     // echo "<a href='?path=Colegios/*'><img src='img/lugares/home.svg'></a>   ";
     //  if($path!="Colegios/*"){
     //     echo "<a href='?path=".$back."'><img src='img/lugares/home.svg'></a>";
     // }
      ?>
        <div class="panel-body">

          <div class="dataTable_wrapper">
            <table class="table table-striped table-bordered table-hover dataTable" id="dataTables-example">
              <thead>
                <tr>
                  <th style="width:32px"></th>
                  <th class="sorting_desc" tabindex="0" aria-controls="dataTables-example" rowspan="1" colspan="1" aria-label="" aria-sort="descending">Nombre</th>
                  <th style="width: 100px;">Tamaño</th>
                  <th style="width: 200px;">Modificado</th>
                </tr>
              </thead>
              <tbody>
                <?php
              for($i=0;$i<count($carpetas);$i++){
                  $link='?path='.$completo[$i].'/*';
                  echo '<tr class="odd gradeX"><td><a href="'.$link.'"><img src="Views/img/archivos/folder.svg" width="32" height="32"></a> </td><td style="vertical-align: middle"><a href="'.$link.'">'.$carpetas[$i].'</a></td><td style="vertical-align: middle">-</td><td style="vertical-align: middle">-</td></tr>';
              };
               for($i=0;$i<count($archivos);$i++){
                  $link='/colinaeduca/'.$completoa[$i];
                  $extencion=substr($completoa[$i], -3, 3); 

                  $extencion=sw($completoa[$i]);
                  $size=calcSize($completoa[$i]);
                  echo '<tr class="odd gradeX"><td><a href="'.$link.'"><img src="Views/img/archivos/'.$extencion.'.svg" width="32" height="32"></a> </td><td style="vertical-align: middle"><a href="'.$link.'">'.$archivos[$i].'</a></td><td style="vertical-align: middle">'.$size.'</td><td style="vertical-align: middle">'.date('d-F-Y H:i:s.',filectime($completoa[$i])).'</td></tr>';
              };  
               
              ?>
              </tbody>
            </table>
            <?php
          if (isset($_FILES['archivo'])) {
       
      //  var_dump($_FILES['archivo']);
       
    # definimos la carpeta destino
    $carpetaDestino='/var/www/html/colinaeduca/'.str_replace('*', '', $path);
 
    # si hay algun archivo que subir
    if($_FILES["archivo"]["name"][0])
    {
        # recorremos todos los arhivos que se han subido
        for($i=0;$i<count($_FILES["archivo"]["name"]);$i++)
        {
            $origen=$_FILES["archivo"]["tmp_name"][$i];
            $destino=$carpetaDestino.$_FILES["archivo"]["name"][$i];
            echo $origen.'--'.$destino;

            # movemos el archivo
            if(@move_uploaded_file($origen, $destino))
            {
                echo "<meta http-equiv=refresh content=1;URL=>";
            }else{
                echo "<br>No se ha podido mover el archivo: ".$_FILES["archivo"]["name"][$i]."<br>";
                echo $origen.'--'.$destino;
            } 
		}
    }else{
        echo "<br>No se ha subido ninguna";
    }
          }
    ?>


          </div>

          <?php
          if($path!="Colegios/*"){
            ?>
          <div class="row" style="text-align: center;" >  
            <div class="col-lg-6">
              <form action="" method="post" enctype="multipart/form-data" style="text-align: center;" name="inscripcion">
                <input type="file" style="text-align: center;" class="btn btn-default" name="archivo[]" multiple="multiple">
            </div>
            <div class="col-lg-6" >
              <input type="submit" value="Subir" class="btn btn-default">
            </div>
            </form>
          </div> 
          <?php } ?>
        </div>

      </div>

    </div>
{% endblock %}