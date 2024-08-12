int missingNumber(int arr[], int n) 
    { 
        int point= 0;
        for (int i = 0; i < n; i++) {
            if (arr[i] == 1) {
                point= 1;
                break;
            }
        }
        if (point== 0)
            return 1;
    
        for (int i = 0; i < n; i++)
            if (arr[i] <= 0 || arr[i] > n)
                arr[i] = 1;
    
      
        for (int i = 0; i < n; i++)
            arr[(arr[i] - 1) % n] += n;
        for (int i = 0; i < n; i++)
            if (arr[i] <= n)
                return i + 1;
    
      return n + 1;
    } 