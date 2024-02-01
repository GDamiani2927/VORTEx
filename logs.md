**Challenges:**  
*Hysteresis-* Also known as electromagnetic saturation, hysteresis is the phenomenon in which after a certain voltage is applied cutting of power comes with inherent delay in loss of magnetism. This delay could be a major issue if a timed release is necessary.  
*Solution-* Unknown for long term, but we hypothesize that this delay will be insignificant for an electromagnet of our size. The issue seems to be scaled for voltage, of which we are not using much (relative to common applications of electromagnets).  
*Conclusion-* Problem only applies to systems between 0.2 and 0.5 Teslas. A Tesla is defined as one weber per square metre. The calculations of this unit for our electromagnet are beyond the scope of this project. That being said, a Tesla is a unit that we would never hope to intentionally reach at an educational facility, so all should be well.

*Electromagnetic Strength-* We are working with a beam of a small diameter, making this into a strong electromagnet is going tobe very difficult, especially given how far out the wiring has to go. Standard "DIY" electromagnets consist of ferrous material wrapped with a whire to generate an electromagnetic field, but these are not very powerful and would involve wiring that is able to spin without twisting.

*Wiring to release mechanism-* The central axle will likely be spinning at RPMS in the 100s, how do we get signals to a release mechanism from the pico stored in the hub?
*Options-* 
Could use a slip ring, which allows for rotational transfer of power/signals. Costs about $15 from adafruit (ID 763). Rated for 300 rpm for a clean signal and 240V @2 amps
Could use a power/controller unit on the rotating axis itself, either underneath or above. Could introduce problems with rotational forces acting on the circuitry.

*
