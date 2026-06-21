public class DynamicArray {

    int[] array;
    int lastElem = 0;
    int capacity = 0;
    
    public DynamicArray(int capacity) {
        if(capacity < 0) return;

        this.array = new int[capacity];
        this.capacity = capacity;
    }

    public int Get(int i) {
        return this.array[i];
    }

    public void Set(int i, int n) {
        this.array[i] = n;
    }

    public void PushBack(int n) {
        if (lastElem == capacity) Resize();
        this.array[lastElem] = n;
        this.lastElem +=1;
    }

    public int PopBack() {
        this.lastElem -=1;
        return this.array[lastElem];
    }

    private void Resize() {
        this.capacity *=2;
        int[] newArray = new int[this.capacity];
        Array.Copy(this.array, newArray, this.lastElem);
        this.array = newArray;
    }

    public int GetSize() {
        return this.lastElem;
    }

    public int GetCapacity() {
        return this.capacity;
    }
}
