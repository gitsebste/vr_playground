using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class DestroyOnProjectile : MonoBehaviour
{
    void OnTriggerEnter(Collider other)
    {
        if (other.gameObject.tag == "projectile")
        {
            Destroy(gameObject);
            Destroy(other);
        }
    }
}
