using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Smietnik : MonoBehaviour
{
    public GameObject gracz;
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    void OnTriggerExit(Collider other) {
     if(other.gameObject.tag == "pilkatenisowa")
     {
        Debug.Log("Pilka w koszu");
	 }
	 Destroy(other.gameObject);
 }
}
