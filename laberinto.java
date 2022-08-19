public class laberinto {
    public static void main(String[] args) {
        // Usa la matriz en lugar del laberinto
        int[][] map = {
            {1,1,1,1,1,1,1,1,1,1},
            {1,0,1,0,0,0,0,0,0,1},
            {1,0,1,0,1,1,1,1,0,1},
            {1,0,1,0,0,0,0,1,0,1},
            {1,0,1,0,1,1,0,1,0,1},
            {1,0,1,0,1,0,0,1,0,1},
            {1,0,1,0,1,0,1,1,0,1},
            {1,0,1,0,1,0,0,1,0,1},
            {1,0,0,0,1,1,0,1,0,1},
            {1,1,1,1,1,1,1,1,1,1}
            };

        // Llame al método de búsqueda de trayectoria de bola pequeña
        setWay(map,1,1);
        // Imprimir mapa
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 10; j++) {
                System.out.print(map[i][j]+" ");
            }
            System.out.println();
        }
    }

    /**
     * @param map
     * @param i
     * @param j
           * @return devuelve verdadero si se encuentra una ruta, de lo contrario devuelve falso
     */
    public static boolean setWay(int[][] map,int i,int j){
        if(map[8][8]==2){
            return true;
        }else{
            if(map[i][j]==0){
                map[i][j]=2;// Suponiendo que el punto puede pasar
                if(setWay(map,i+1,j)){//Bajar
                    return true;
                }else if(setWay(map,i,j+1)){//Ve a la derecha
                    return true;
                }else if(setWay(map,i-1,j)){//Subir
                    return true;
                }else if(setWay(map,i,j-1)){//girar a la izquierda
                    return true;
                }else{
                    // Es un callejón sin salida en este punto
                    map[i][j]=3;
                    return false;
                }
            }else{//map[i][j]!=0
                return false;
            }
        }
    }
}